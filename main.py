from fastapi import FastAPI,Path,Query
from typing import Annotated
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse,FileResponse,PlainTextResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI() #FastAPI 物件


#非靜態檔案處理的路由，處在上方
@app.get("/square")
def square(num:Annotated[int,None]):
    result=num*num
    return {"data":result}

@app.get("/member")
def member():
    return RedirectResponse("https://www.google.com/")

#統一處理靜態檔案 擺在下方才不會影響其他的路由
app.mount("/",StaticFiles(directory="public",html=True))



