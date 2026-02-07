from flask import Flask, request, jsonify
import os

from src.data_loader import load_incidents
from src.semantic_engine import SemanticSimilarityEngine

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "resolved_incidents.csv")

SIMILARITY_THRESHOLD = 0.60

# Load historical incidents
df = load_incidents(DATA_PATH)

# Initialize semantic similarity engine
engine = SemanticSimilarityEngine(df["combined_text"].tolist())


@app.route("/match", methods=["POST"])
def match_incident():
    data = request.json

    new_text = (
        data.get("short_description", "") + " " +
        data.get("category", "") + " " +
        data.get("cmdb_ci", "") + " " +
        data.get("description", "")
    )

    index, score = engine.find_best_match(new_text)

    if score < SIMILARITY_THRESHOLD:
        return jsonify({
            "message": "No similar incident found",
            "similarity_score": score
        })

    matched = df.iloc[index]

    return jsonify({
        "matched_incident": matched["number"],
        "assignment_group": matched["assignment_group"],
        "similarity_score": score
    })


if __name__ == "__main__":
    app.run(port=5000)
