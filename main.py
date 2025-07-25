from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Actually Useful AI is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    user_prompt = data.get("prompt", "")
    search_result = data.get("search", "")

    if not user_prompt or not search_result:
        return jsonify({"error": "Both 'prompt' and 'search' are required."}), 400

    # 👇🏽 AI logic: for now, basic formatting. We can add real AI later.
    improved_response = f"""Here's a clearer explanation of your request:

🔍 You asked: "{user_prompt}"
🧠 Based on search: "{search_result}"

📘 Here's a refined summary:
{refine_answer(user_prompt, search_result)}
"""
    return jsonify({"response": improved_response})


def refine_answer(prompt, search):
    # ✨ Simple mock of refinement – can replace with GPT API later
    return f"{search}. This information directly addresses your query: '{prompt}'."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
