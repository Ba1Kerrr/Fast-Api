from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
@app.get("/")

async def home():
   return {"data": "Hello World"}


class STaskAdd(BaseModel):
   name: str
   description: str | None = None

@app.post("/")
async def add_task(task: STaskAdd):
   return {"data": task}