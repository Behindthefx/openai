from fastapi import FastAPI
import json

app = FastAPI()

# Load the NGSS data once at startup
with open("ngss.json", "r") as f:
    ngss_data = json.load(f)

@app.get("/ngss")
def search_ngss(topic: str, grade: str):
    matches = [
        item for item in ngss_data
        if topic.lower() in item["description"].lower() and item["grade"] == grade
    ]
    return {"results": results}

