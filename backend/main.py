
from fastapi import FastAPI, HTTPException, Request
from starlette.responses import RedirectResponse
from models import Base, Link
from database import engine, SessionLocal
from crud import create_link, get_link_by_code, list_links, delete_link
import string, random

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/api/shorten")
def shorten_url(payload: dict):
    db = SessionLocal()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    link = create_link(db, code, payload["url"])
    return {
        "short_url": f"http://short.local/{code}",
        "original_url": payload["url"]
    }

@app.get("/{short_code}")
def redirect(short_code: str, request: Request):
    db = SessionLocal()
    link = get_link_by_code(db, short_code)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return RedirectResponse(url=link.original_url, status_code=302)

@app.get("/api/links")
def get_links():
    db = SessionLocal()
    return list_links(db)

@app.delete("/api/links/{short_code}")
def delete(short_code: str):
    db = SessionLocal()
    delete_link(db, short_code)
    return {"message": "Link deleted successfully"}
