from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
from database.database import SessionLocal
from schemas.blog import BlogSchema, BlogCreate
from services.blog import get_blogs, create_blog, get_blog

router = APIRouter(prefix="/blog", tags=["blog"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
def get_all(db: Session = Depends(get_db)):
    blog = get_blogs(db)
    return blog


@router.get("/{blog_id}", response_model=schemas.blog.BlogSchema)
def find_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog(db, blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="blog not found")
    return blog


@router.post('/')
def create(blog: BlogCreate, db: Session = Depends(get_db)):
    create_blog(db, blog)
    return blog
