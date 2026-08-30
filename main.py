from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.phi3 import router as phi3_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(phi3_router)

@app.get("/")
async def root():
    return {
        "message" : "Hello, from fastapi"
    }