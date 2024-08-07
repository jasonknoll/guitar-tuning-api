from fastapi import FastAPI
import os
from dotenv import load_dotenv

# TODO turn this into the "Jason API" instead of just about guitar

load_dotenv()

app = FastAPI()

# TODO - Pick new database/ask gpt


VERSION = "v1"
MUSIC_PREFIX = f"/{VERSION}/music"
CRYPTO_PREFIX = f"/{VERSION}/crypto"

@app.get("/")
async def index():
    return {"out":"API is online!"}

# TODO add more endpionts haha
@app.get(f"{MUSIC_PREFIX}/guitar/")
async def get_guitar_index():
    return {"out":"This will be a damn api soon. Need to plan DB schema"}

@app.get(f"{MUSIC_PREFIX}/guitar/tunings")
async def get_guitar_tunings():
    return {"":""}

@app.get(f"{MUSIC_PREFIX}/bands/")
async def get_bands():
    return {"":""}

@app.get(f"{MUSIC_PREFIX}/songs/")
async def get_songs():
    return {"":""}

# ----Crypto endpoints----
@app.get(f"{CRYPTO_PREFIX}/")
async def crypto_index():
    return {"out":"Check out api.jasonknoll.net/docs for help!"}

