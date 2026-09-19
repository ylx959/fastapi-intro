from fastapi import FastAPI,Body
import json

app=FastAPI()

# 在前端先把json 轉為string 傳進後端 再把 string 用json.load(string)
# 轉成json去做應用


# <button onclick="connectPost();">POST連線</button>
#         <script>
#             async function connectPost(){
#                 let response=await fetch("/add",{
#                     method:"POST",
#                     body:JSON.stringify({"n1":5,"n2":3})
#                 });
#                 let data=await response.json();
#                 console.log(data)
#             }
#         </script>

#處理post 方法的路徑/test
@app.post("/test")
def testPost(body=Body(None)):
    data=json.loads(body)
    print(body)
    return {"ok":True,"method":"POST","result":data["x"]}

#處理post 方法的路徑/add
@app.post("/add")
def testPost(body=Body(None)):
    data=json.loads(body)
    print(body)
    ans=data["n1"]+data["n2"]
    return {"ok":True,"method":"POST","result":ans}

