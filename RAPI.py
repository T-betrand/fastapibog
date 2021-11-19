from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

app = FastAPI()


#get all the blogs -> blog list
@app.get("/")
def index():
    return {"data": "blog list"}

#unpulished blog
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished blog list"}

#query param
@app.get("/blog")
def index2(limit, published: bool):
    if published is True:
        return {"data": f'{limit} published blogs from the database'}
    return {"data": f'{limit} blogs from the db'}


#getting a specific blog
@app.get("/blog/{blog_id}")
def show(blog_id: int):
    return {"blog": blog_id}


#getting blogs and comments
@app.get("/blog/{blog_id}/comments")
def comments(blog_id: int):
    return {
        "data": {
            "blog id": blog_id,
            "blog comment": "fixed"
        }
    }

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post("/blog")
def create_blog(blog: Blog):
    return {"message": f"blog {blog.title} created"}











# @app.get("/")
# async def max():
#         return {
#             "data": {
#                 "name": "fench",
#             }
#         }

# @app.get("/about")
# def about():
#     return {"data": {"name": "Betrand"}}