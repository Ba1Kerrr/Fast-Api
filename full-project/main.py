from fastapi import FastAPI, Body,Request
from fastapi.responses import FileResponse
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("static/Home.html")

@app.post("/hello")
def hello(data = Body()):
    name = data["name"]
    age = data["age"]
    return {"message": "Hello World"}

