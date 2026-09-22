# <h2>留言系統</h2>
#     <div>
#         姓名<input type="text" id="name"/>
#         <br/>
#         內容<input type="text" id="content"/>
#         <br/>
#         <button onclick="postMessage()">送出</button>
#         <hr/>
#     </div>
#     <div id="board"></div>
#     <script>
#         async function postMessage(){
#             let name=document.querySelector("#name").value;
#             let content=document.querySelector("#content").value;

#             let response=await fetch("api/message",{method:"Post",body:JSON.stringify({"author":name,"content":content})});
#             let result=await response.json();
#             if(result.ok){
#                 getMessage();
#             }
#             console.log(result);
#         }
#         async function getMessage(){
#             let response=await fetch("api/message",{method:"get"});
#             let result=await response.json();
#             let board=document.querySelector("#board");
#             board.innerHTML="";
#             for(let i=0;i<result.length;i++){
#                 board.innerHTML+="<div>"+result[i].author+": "+result[i].content+"<button onclick='deleteMessage("+result[i].id+")'>X</button>"+"</div>";
#             }
#             console.log(result);
#         }
#         async function deleteMessage(id){
#             let response=await fetch("api/message/"+id,{method:"delete"});
#             let result=await response.json();
#             if(result.ok){
#                 getMessage();
#             }
#             console.log(result);
#         }
#         getMessage();
#     </script>

import json

from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles

# 準備資料庫連線
import mysql.connector
con = mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="fastapi"
)

print("DataBase Ready")

app = FastAPI()


# 新增留言 API
@app.post("/api/message")
def create_message(body=Body(None)):
    # 預期收到：
    # {"author": "name", "content": "內容"}

    body = json.loads(body)

    author = body["author"]
    content = body["content"]

    cursor = con.cursor()

    cursor.execute(
        "INSERT INTO message(author, content) VALUES (%s, %s)",
        [author, content]
    )
    
    con.commit()

    return {"ok": True}
    #這樣就完成一個api

#取得所有留言的api
@app.get("/api/message")
def get_message():
    cursor=con.cursor(dictionary=True)
    cursor.execute("select * from message")
    data=cursor.fetchall()
    return data

#刪除留言的api
@app.delete("/api/message/{id}")
def delete_message(id):
    cursor=con.cursor()
    cursor.execute("delete from message where id=%s",[id])
    con.commit()

    return {"ok":True}



# 靜態檔案
app.mount("/", StaticFiles(directory="public", html=True))