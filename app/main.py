from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name ="nothing"
number= 0


@app.post("/")
def create_item(item_id: str,q: int):
    name = item_id
    number = q   
    return {"item_id": name, "q": number}

@app.get("/")
def read_item():
    return {"item_id": name, "q": number}

@app.put("/")
def update_item(item_id: str,q: int):
    name = item_id
    number = q
    return {"item_id": name, "q": number}

@app.delete_item("/")
def read_item(item_id: str, q: int):
    name = "nothing"
    number = 0
    return {"item_id": item_id, "q": q}

