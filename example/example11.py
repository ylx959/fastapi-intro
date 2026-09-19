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

#搭配前端

# <h2>使用fetch 測試restful APIS%</h2>
#     <button onclick="postMessage();">Post message</button>
#     <button onclick="getMessage();">Get message</button>
#     <button onclick="deleteMessage();">Delete message</button>
#     <script>
#         async function postMessage(){
#             let response=await fetch("api/message",{method:"Post",body:JSON.stringify({"author":"John","content":"測試"})});
#             let result=await response.json();
#             console.log(result);
#         }
#         async function getMessage(){
#             let response=await fetch("api/message",{method:"get"});
#             let result=await response.json();
#             console.log(result);
#         }
#         async function deleteMessage(){
#             let response=await fetch("api/message/5",{method:"delete"});
#             let result=await response.json();
#             console.log(result);
#         }
#     </script>

