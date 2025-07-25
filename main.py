from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is working!"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return jsonify({"query_received": query})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
