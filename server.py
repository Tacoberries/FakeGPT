import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
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
        messages=[{"role": "system", "content": "Você é uma ajudante virtual chamada Mia."},
                  {"role": "user", "content": message}],
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)

