# <h2>發送Request測試結果</h2>
#     <div>
#         <button onclick="hello();">Hello</button>
#         <button onclick="talk();">Talk</button>
#     </div>
#     <script>
#         async function hello(){
#             let response=await fetch("/hello?name=John",{method:"get"});
#             let result=await response.json();
#             console.log(result);
#         }
#         async function talk(){
#             let response=await fetch("/talk",{method:"get"});
#             let result=await response.json();
#             console.log(result);
#         }
#     </script>

from fastapi import FastAPI, Request,Body
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="greee")


# 新增留言 API
@app.get("/hello")
def hello(name:str,request:Request):
  
    request.session["data"]=name

    return {"message":"hello,"+name }
    #這樣就完成一個api

#取得所有留言的api
@app.get("/talk")
def talk(request:Request):
    name=request.session["data"]
    return {"message":"How are you "+name}

# 靜態檔案
app.mount("/", StaticFiles(directory="public", html=True))