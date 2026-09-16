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



