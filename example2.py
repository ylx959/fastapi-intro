# from fastapi import FastAPI

# app=FastAPI() #FastAPI 物件
# #利用uvicron 去啟動伺服器在 http://127.0.0.1:8000
# #利用route的設定.處理路徑/
# @app.get("/")
# def index():
#     return {"data":"Home Page"}

# #利用路由設定 處理路徑/data
# @app.get("/data")
# def getData():
#     return {"data":[2,3,4]}

# #想要讓前端可以透過網址，輸入一個數字再把輸入數字做平方,再回應給前端
# #路徑參數 處理有相同前綴字/square/任意的整數 的路徑
# @app.get("/square/{number}")
# def square(number):
#     number=int(number) 
#     return {"result":number*number}