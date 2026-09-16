from fastapi import FastAPI
from typing import Annotated
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse,FileResponse,PlainTextResponse

app=FastAPI() #FastAPI 物件
#利用uvicron 去啟動伺服器在 http://127.0.0.1:8000
#利用route的設定.處理路徑/

#利用JSONResponse
@app.get("/")
def index():
    return JSONResponse({"data":[2,3,4],"title":"My data"})

@app.get("/text")
def text():
    return PlainTextResponse("I love to eat hambuger")

@app.get("/web")
def web():
    return HTMLResponse("""
    <h2>Author</h2>
    <p>I love to eat beef,pork</p>
    <a href=mailto:yanglinxuan0421@gmail.com>gmail</a>""")

@app.get("/html")
def html():
    return FileResponse("home.html")

@app.get("/img/logo")
def logo():
    return FileResponse("test.png")

@app.get("/member")
def member():
    return RedirectResponse("https://www.google.com/")
