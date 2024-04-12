from fastapi import FastAPI

app = FastAPI()

 

@app.get("/")
def root():
    return {"Message": "Hello root"}


@app.get("/home")
def home():
    return {"Message": "Home!"}