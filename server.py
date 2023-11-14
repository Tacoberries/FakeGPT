import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, render_template, request

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": message}],
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)
