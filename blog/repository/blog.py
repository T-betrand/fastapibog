from fastapi import HTTPException, status
from fastapi.param_functions import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user

from blog.oauth2 import get_current_user
from .. import models, schemas




def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no blog with id {id} found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted"


def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no blog with id {id} found")
    blog.update(request, db)
    db.commit()
    return "Updated"

def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no blog with id {id} found")
    return blog