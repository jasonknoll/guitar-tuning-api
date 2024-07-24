from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# TODO - Pick new database/ask gpt

@app.get("/")
async def index():
    return {"out":"API is online!"}

# TODO add more endpionts haha

