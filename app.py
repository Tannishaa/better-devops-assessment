from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "The best way to predict the future is to create it.",
    "DevOps is not a goal, but a never-ending process of continual improvement.",
    "The only way to do great work is to love what you do.",
    "Automate everything that can be automated.",
    "Move fast and break things... but have a good rollback plan."
]

@app.route("/")
def get_quote():
    """Returns a random quote in JSON format."""
    quote = random.choice(QUOTES)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)