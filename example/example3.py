from fastapi import FastAPI

app=FastAPI() #FastAPI 物件
#利用uvicron 去啟動伺服器在 http://127.0.0.1:8000
#利用route的設定.處理路徑/
@app.get("/")
def index():
    return {"data":"Home Page"}

#處理路徑/hello?name=名字
@app.get("/hello")
def hello(name):
    message="哈囉"+name
    return {"message":message}

#處理路徑 /multiply ?n1=數字&n2=數字
@app.get("/multiply")
def multiply(n1,n2):
    n1=int(n1)
    n2=int(n2)
    calculate=n1*n2
    return {"answer":calculate}