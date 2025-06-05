from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load NGSS data on startup
with open("ngss.json") as f:
    standards = json.load(f)

@app.route("/ngss", methods=["GET"])
def get_ngss():
    grade = request.args.get("grade", "").strip().lower()
    topic = request.args.get("topic", "").strip().lower()

    if not grade or not topic:
        return jsonify({"error": "Missing grade or topic"}), 400

    # Filter standards by grade and topic keyword
    matches = []
    for std in standards:
        std_grade = std.get("grade", "").lower()
        std_desc = std.get("description", "").lower()

        if grade in std_grade and topic in std_desc:
            matches.append({
                "code": std.get("code", "N/A"),
                "description": std.get("description", "No description available")
            })

    return jsonify({"standards": matches})
