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

    contents = requests.get(URL).text
    
    return { "message": contents}

@app.get("/home")
def home():
    return { "message": "Home!" }