from flask import Flask, request, jsonify
import duckduckgo_search
import google.generativeai as genai

app = Flask(__name__)

@app.route('/ai', methods=['POST'])
def ai():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Missing query"}), 400

    # DuckDuckGo search
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.text(user_query, max_results=5)
        snippets = "\n".join([r["body"] for r in results if "body" in r])

    # Combine prompt and search
    prompt = f"User asked: {user_query}\nHere are relevant facts:\n{snippets}\nNow explain clearly:"
    
    genai.configure(api_key="YOUR_GEMINI_API_KEY")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return jsonify({"result": response.text})

if __name__ == '__main__':
    app.run()
