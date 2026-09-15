from fastapi import FastAPI

app=FastAPI() #FastAPI 物件

@app.get("/")

def index():
    return {"x":3, "y":4}

