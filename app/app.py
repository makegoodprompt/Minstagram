from fastapi import FastAPI
app = FastAPI()

text_posts = {
    1:{
        "title" : "First Post Title",
        "content" : "Second Post Content",
    },
    2:{
        "title" : "Second Post Title",
        "content" : "Third Post Content",
    }
}

@app.get("/posts")
def read_all_posts():
    return text_posts

@app.get("/posts/{id}")
def read_post(id: int):
    return text_posts.get(id)