from sqlalchemy.orm import Session
from schemas.blog import BlogCreate
from models import models


def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def create_blog(db: Session, blog: BlogCreate):
    db_blog = models.Blog(body=blog.body, title=blog.title)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
