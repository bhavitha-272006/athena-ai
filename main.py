from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class LoginRequest(BaseModel):
    username:str
    password:str
@app.post("/login")
def login(user:LoginRequest):
    return{
        "username":user.username,
        "password":user.password,
        "success": True,
        "message": "Login Successful",
        }
