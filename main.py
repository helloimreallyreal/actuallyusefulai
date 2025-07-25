from flask import Flask, request, jsonify
from duckduckgo_search import DDGS

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is working!"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    if not prompt:
        return jsonify({"error": "No prompt received"}), 400

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(prompt, max_results=3):
            results.append(r["body"])
    
    joined_result = "\n".join(results)
    
    # Simulate "AI polishing" here
    polished = f"🧠 Here's a clearer explanation:\n{joined_result}"
    
    return jsonify({"result": polished})

if __name__ == '__main__':
    app.run()
