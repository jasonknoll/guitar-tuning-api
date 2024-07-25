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
@app.get("/v1/guitar/")
async def get_guitar_index():
    return {"out":"This will be a damn api soon. Need to plan DB schema"}

@app.get("/v1/guitar/tunings")
async def get_guitar_tunings():
    return {"":""}

@app.get("/v1/bands/")
async def get_bands():
    return {"":""}

@app.get("/v1/songs/")
async def get_songs():
    return {"":""}

