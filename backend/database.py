import sys
from config import settings
from pymongo import MongoClient, errors

ATLAS_CONNECTION: str = f"mongodb+srv://bjjaiswal:{settings.mongodb_pass}@origin.ztyhi98.mongodb.net/?retryWrites=true&w=majority"


try:
    client = MongoClient(ATLAS_CONNECTION)

# return a friendly error if a URI error is thrown
except errors.ConfigurationError:
    print(
        "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
    )
    sys.exit(1)

db = client.blog_db
blogs_collection = db["blog_post"]


dummy_data = [
    {
        "id": "the-art-of-programming",
        "title": "The Art of Programming",
        "author": "John Doe",
        "content": "Programming is both an art and a science. In this blog post, we explore the creative aspects of coding and how it intersects with technology.",
        "publication_date": "2023-09-16",
    },
    {
        "id": "getting-started-with-python",
        "title": "Getting Started with Python",
        "author": "Jane Smith",
        "content": "Python is a versatile and beginner-friendly programming language. In this tutorial, we'll cover the basics of Python programming.",
        "publication_date": "2023-09-15",
    },
    {
        "id": "the-future-of-artificial-intelligence",
        "title": "The Future of Artificial Intelligence",
        "author": "David Johnson",
        "content": "Artificial Intelligence is changing the world. In this blog post, we discuss the current state of AI and what the future holds.",
        "publication_date": "2023-09-14",
    },
    {
        "id": "web-development-trends-in-2023",
        "title": "Web Development Trends in 2023",
        "author": "Sarah Brown",
        "content": "Web development is evolving rapidly. Find out what trends are shaping the web development landscape in 2023.",
        "publication_date": "2023-09-13",
    },
    {
        "id": "exporing-the-cosmos",
        "title": "Exploring the Cosmos",
        "author": "Michael Anderson",
        "content": "Astronomy has always fascinated humanity. Join us on a journey through the cosmos as we explore the wonders of space.",
        "publication_date": "2023-09-12",
    },
]
