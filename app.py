from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Bloom with grace, even in the spaces you didn't think you'd grow.",
    "Your only limit is the one you set in your own sky.",
    "Create a life that feels as good on the inside as it looks on the outside.",
    "Trust the magic of new beginnings and the detours along the way.",
    "Be the energy you want to attract: vibrant, brave, and unapologetically you.",
]

@app.route("/")
def get_quote():
    """Returns a random quote in JSON format."""
    quote = random.choice(QUOTES)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)