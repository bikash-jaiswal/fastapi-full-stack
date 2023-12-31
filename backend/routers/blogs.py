import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from backend.models.blogs import BlogModel
from backend.database import blogs_collection, dummy_data

CURRENT_YEAR = datetime.date.today().year

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")


@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "year": CURRENT_YEAR}
    )


@router.get(
    "/blogs", response_description="list of all blogs", response_model=List[BlogModel]
)
async def get_blog_posts(request: Request):
    # Specify the fields to include in the projection
    projection = {"title": 1, "author": 1, "_id": 0}

    # Retrieve all blog posts from the MongoDB collection
    all_posts = list(blogs_collection.find({}, projection))

    # If there are no blog posts, return an empty list
    if not all_posts:
        return []

    return templates.TemplateResponse(
        "blogs.html", {"request": request, "data": all_posts, "year": CURRENT_YEAR}
    )


@router.post(
    "/blogs/", response_description="Add multipe posts", response_model=list[BlogModel]
)
async def add_multiple_new_posts(posts: list[BlogModel] = dummy_data):
    # Convert the incoming list of blog post data to a list of dictionaries
    posts_data = [jsonable_encoder(post) for post in posts]

    # Insert the list of post data into the MongoDB collection
    result = blogs_collection.insert_many(posts_data)

    # Get the newly inserted documents' IDs
    new_post_ids = result.inserted_ids

    # Return a JSON response with the IDs of the new posts
    return JSONResponse(content={"message": f"Multiple post has been added"})


# @router.post("/blogs/", response_description="Add new post", response_model=BlogModel)
# async def add_new_post(post: BlogModel):
#     # Convert the incoming blog post data to a dictionary
#     post_data = jsonable_encoder(post)

#     # Insert the post data into the MongoDB collection
#     result = blogs_collection.insert_one(post_data)

#     # Get the newly inserted document's ID
#     new_post_id = result.inserted_id

#     # Return a JSON response with the new post's ID
#     return JSONResponse(content={"message": f"New data has been added with id={new_post_id}"})


@router.get(
    "/blogs/{post_id}",
    response_description="Get a specific post",
    response_model=BlogModel,
)
async def get_blog_post_by_id(post_id: str):
    # Find the blog post by its ID
    post_data = blogs_collection.find_one({"id": post_id})

    if post_data is None:
        raise HTTPException(status_code=404, detail="Blog post not found")

    return post_data
