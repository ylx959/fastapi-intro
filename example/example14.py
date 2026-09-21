#  <h2>發送Requests測試結果</h2>
#     <div>
#         <button onclick="signup()">註冊帳號</button>
#         <button onclick="signin()">登入帳號</button>
#         <button onclick="checkstatus()">檢查登入狀態</button>
#         <button onclick="signout()">登出</button>
#     </div>
#     <script>
#         async function signup(){
#             let response=await fetch("/api/member",{
#                 method:"post",
#                 body:JSON.stringify({"name":"ply","email":"ply@ply.com","password":"ply"})

#             });
#             let result=await response.json();
#             console.log("註冊結果",result);
#         }
#         async function signin(){
#             let response=await fetch("/api/member/auth",{
#                 method:"PUT",
#                 body:JSON.stringify({"email":"ply@ply.com","password":"ply"})

#             });
#             let result=await response.json();
#             console.log("註冊結果",result);
#         }
#         async function checkstatus() {
#             let response=await fetch("/api/member/auth",{
#                 method:"GET",
#             });
#             let result=await response.json();
#             console.log("登入狀態",result);
#         }
#         async function signout() {
#             let response=await fetch("/api/member/auth",{
#                 method:"DELETE",
#             });
#             let result=await response.json();
#             console.log("登出狀態",result);
#         }
#     </script>

#準備資料庫連線
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="fastapi"
)

print("Database Ready")

from fastapi import FastAPI, Request,Body
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import json

#建立fastapi物件
app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="grgergg2")

@app.post("/api/member")
def signup(body=Body(None)):
    body=json.loads(body)
    name=body["name"]
    email=body["email"]
    password=body["password"]

    #check whether the email is repeated
    cursor=con.cursor()
    cursor.execute("Select * from member where email=%s",[email])
    result=cursor.fetchone()
    if result==None:
        cursor.execute("INSERT into member(name,email,password) values(%s,%s,%s)",[name,email,password])
        con.commit()
        return {"ok":True}
    else:#代表email重複
        return {"ok":False}

#登入帳號的api
@app.put("/api/member/auth")
def signin(request:Request,body=Body(None)):
    body=json.loads(body)
    email=body["email"]
    password=body["password"]

    cursor=con.cursor()
    cursor.execute("Select * from member where email=%s and password=%s",[email,password])
    result=cursor.fetchone()

    if result==None:
        request.session["member"]=None
        return {"ok":False}
    else:
        request.session["member"]={"name":result[1],"email":result[2]}
        return {"ok":True}

#檢查登入狀態的api
@app.get("/api/member/auth")
def check_status(request:Request):
    if "member" in request.session and request.session["member"]!=None:
        member=request.session["member"]
        return {"ok":True,"name":member["name"],"email":member["email"]}
    else:
        return {"ok":False}
#登出
@app.delete("/api/member/auth")
def signout(request:Request):

    request.session["member"]=None
    return {"ok":True}


# 靜態檔案
app.mount("/", StaticFiles(directory="public", html=True))



