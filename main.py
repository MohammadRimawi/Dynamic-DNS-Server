

from fastapi import FastAPI,Body,Response,status,Request
import uvicorn
from LinuxHostsManager import update_host_interface
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = FastAPI()
PASSWORD = getenv("PASSWORD")
PORT = int(getenv("PORT"))

@app.put("/")
def index(
        response:Response,
        request:Request,
        password:str = Body(default=None,embed=True),
        domain:str = Body(default=None,embed=True),
        ip:str = Body(default=None,embed=True)
        ):
    """"""
    # print(request)
    if password != PASSWORD :
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"response":"Failed"}
    try:
        update_host_interface(host_name=domain,host_ip=ip)
    except Exception() as e:
        response.status_code = status.HTTP_400_BAD_REQUEST 
        return {"response":"Failed"}
    return {"response":"Confirm"}

if __name__ =="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=PORT,reload=True) 
