from fastapi import FastAPI,Path,Query,Body
from typing import Annotated
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse,FileResponse,PlainTextResponse
from fastapi.staticfiles import StaticFiles
import json
app=FastAPI() #FastAPI 物件

#非靜態檔案處理的路由，處在上方
#處理get方法得路徑/test
@app.get("/test")
def testGET():
    return {"data":10,"method":"GET"}

#處理post 方法的路徑/add
@app.post("/add")
def testPost(body=Body(None)):
    data=json.loads(body)
    print(body)
    ans=data["n1"]+data["n2"]
    return {"ok":True,"method":"POST","result":ans}


@app.get("/square")
def square(number:Annotated[int,Query(gt=0,lt=100)]):
    result=number*number
    return {"data":result}

@app.get("/multiply")
def multiply(n1:Annotated[int,None],n2:Annotated[int,None]):
    result=n1*n2
    return {"result":result}

@app.get("/member")
def member():
    return RedirectResponse("https://www.google.com/")

#統一處理靜態檔案 擺在下方才不會影響其他的路由
app.mount("/",StaticFiles(directory="public",html=True))





