from fastapi import FastAPI,Path,Query
from typing import Annotated

app=FastAPI() #FastAPI 物件
#利用uvicron 去啟動伺服器在 http://127.0.0.1:8000
#利用route的設定.處理路徑/
@app.get("/")
def index():
    return {"data":"Home Page"}

from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

#處理路徑 /square/number
@app.get("/square/{number}")
def square(
    number: Annotated[int, Path(gt=0, lt=100)]
):
    result = number * number
    return {"result": result}

#處理路徑 /multiply?n1=number&n2=number
@app.get("/multiply")
def multiply(n1:
             Annotated[int,Query(ge=0,le=100)],
             n2:
             Annotated[int,Query(ge=0,le=100)]):
    n1=int(n1)
    n2=int(n2)
    result=n1*n2
    return {"result":result}

#處理路徑/echo/名字
@app.get("/echo/{name}")
def echo(name:Annotated[str,Path(min_length=2,max_length=30)]):
    return {"reply":"Hello "+name}

#處理字串/hello?name=名字
@app.get("/hello")
def hello(name:Annotated[str,Query(min_length=2,max_length=10)]):
    return {"reply":"Hello "+name}