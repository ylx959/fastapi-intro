#準備好資料庫連線
import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="fastapi"
)

print("DataBase Ready")

#準備網站後端系統
from typing import Annotated
from fastapi import FastAPI
app=FastAPI()

@app.get("/createMessage")
def createMessage(
    author:Annotated[str,None],
    content: Annotated[str,None]
    ):
    #利用已經建立的資料庫連線 對資料庫下 sql 指令
    cursor=con.cursor()
    cursor.execute("INSERT into message(author,content) values(%s,%s)",[author,content])
    con.commit()
    return {"ok":True}