from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Backend running!"

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('query')
    # Placeholder response — replace with real DuckDuckGo + Gemini logic
    return jsonify({
        "answer": f"You asked: {user_input}. This is where the AI answer will go."
    })

if __name__ == '__main__':
    app.run()
