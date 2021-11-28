from fastapi import APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from .. repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
   return user.create(request, db)


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update():
    return user.update()


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy():
    return user.destroy()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def get_all(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)