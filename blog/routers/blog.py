from blog.oauth2 import get_current_user
from .. import schemas, database, oauth2
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

# --> debug notice blog has no attribute items()
@router.put("/{id}", status_code=status.HTTP_200_OK)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get("/", status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.get(id, db)