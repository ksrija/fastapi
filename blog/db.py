from pymongo import MongoClient

# by default connect to the local host
conn = MongoClient(
    'mongodb+srv://srija:N4JwyzOBJ7yW3kxA@cluster0.jg7b3zi.mongodb.net/?retryWrites=true&w=majority')

db = conn.blog_app

collection_name = db["blog_app"]
collection_name_1 = db["users"]
