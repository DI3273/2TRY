from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import requests

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# 미리 생성한 빈 객체를 관리하기 위한 딕셔너리
items = {}

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=110&bizCd=C&apiKey=9y8h8TX0vKGMY6hMRibiurfOGfySlt08cx43AN8x&returnType=json"
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return items[item_id]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q, "item": items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"item_id": item_id, "item": items[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}
