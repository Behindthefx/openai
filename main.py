from fastapi import FastAPI
import json

app = FastAPI()

# Load cleaned NGSS data
with open("ngss_clean.json", "r") as f:
    ngss_data = json.load(f)

@app.get("/")
def root():
    return {"message": "NGSS API is live. Try /ngss?topic=motion&grade=5"}

@app.get("/ngss")
def get_ngss(topic: str, grade: str):
    matches = [
        item for item in ngss_data
        if topic.lower() in item["description"].lower() and item["grade"] == grade
    ]
    return {"results": matches}
