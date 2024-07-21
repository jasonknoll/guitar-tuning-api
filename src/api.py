from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

auth_path = os.getenv("AUTH_PATH")

creds = credentials.Certificate(auth_path)
firebase_admin.initialize_app(creds)
db = firestore.client()

@app.get("/")
async def index():
    return {"out":"Hello World"}

@app.get("/test")
async def test():
    document = db.collection("songs").document("test")
    doc = document.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {"error" : "you idiot"}


