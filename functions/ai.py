import json
from duckduckgo_search import DDGS
import google.generativeai as genai

def handler(event, context):
    try:
        body = json.loads(event['body'])
        query = body.get('query', '')

        if not query:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Query is missing'})
            }

        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            snippets = "\n".join([r["body"] for r in results if "body" in r])

        prompt = f"User asked: {query}\nHere are relevant facts:\n{snippets}\nNow explain clearly:"

        #genai.configure(api_key="YOUR_GEMINI_API_KEY")
        #model = genai.GenerativeModel("gemini-pro")
        #response = model.generate_content(prompt)

        response_text = f"You asked: {query}. DuckDuckGo said:\n{snippets}"


        return {
            'statusCode': 200,
            'body': json.dumps({'result': response.text})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

handler = handler
