from fastapi import FastAPI

app = FastAPI()

# Fake DB
books = [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"Eragon", "available":False},
    {"id":3, "title":"The Hobbit", "available":True}
]

# Home Route
@app.get("/")
def home():
    return {"message":"Nirosh's Library API"}

# Get All Book
@app.get("/books")
def get_book():
    # connect to db
    # run a SQL query
    # get outputs
    # tidy 
    # format and return.
    return books