
from models import Link

def create_link(db, code, url):
    link = Link(code=code, original_url=url)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

def get_link_by_code(db, code):
    return db.query(Link).filter(Link.code == code).first()

def list_links(db):
    return db.query(Link).all()

def delete_link(db, code):
    link = get_link_by_code(db, code)
    if link:
        db.delete(link)
        db.commit()
