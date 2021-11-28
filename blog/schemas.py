from pydantic import BaseModel
from . models import Blog
from typing import List, Optional


#USER SCHEMAS
class User(BaseModel):
    name: str
    email: str
    password: str

    class Config():
        orm_mode = True


#BLOG
class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


#USER SCHEMAS
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


#BLOG
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


#LOGIN
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None