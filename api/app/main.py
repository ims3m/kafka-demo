from fastapi import FastAPI
from app.routes import auth

app  = FastAPI(title= "Auth API", version="1.0.0")

app.include_router(auth.router)

@app.get("/")
async def root():
    return {
        "message":"App is running...",
        "status_code":200
        }
