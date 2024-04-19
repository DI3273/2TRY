from fastapi import FastAPI

import requests 

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2023&month=11&metroCd=11&apiKey=9y8h8TX0vKGMY6hMRibiurfOGfySlt08cx43AN8x&returnType=json"

    contents = requests.get(URL).text
    
    return { "message": contents}

@app.get("/home")
def home():
    return { "message": "Home!" }