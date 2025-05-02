
from sqlalchemy import Column, String, Integer
from database import Base

class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    original_url = Column(String)
    clicks = Column(Integer, default=0)
