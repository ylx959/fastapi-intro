from fastapi import FastAPI,Path,Query
from typing import Annotated
from fastapi.responses import JSONResponse,HTMLResponse,RedirectResponse,FileResponse,PlainTextResponse
from fastapi.staticfiles import StaticFiles

app=FastAPI() #FastAPI 物件

#非靜態檔案處理的路由，處在上方
#處理get方法得路徑/test
@app.get("/test")
def testGET():
    return {"data":10,"method":"GET"}
#處理post 方法的路徑/test
@app.post("/test")
def testPost():
    return {"ok":True,"method":"POST"}

#主要在說明用前端js 可以用不同方法接到後端
# <script>
#     async function connectGet(){
#         let response=await fetch("/test",{method:"可以用GET 或是POST"});
#         let data=await response.json();
#         console.log(data)
#     }
# </script>
