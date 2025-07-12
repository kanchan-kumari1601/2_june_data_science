from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["problem"]
        prompt = f"Solve this math problem step by step: {user_input}"
        try:
            payload = {
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
            res = requests.post(OLLAMA_URL, json=payload)
            if res.status_code == 200:
                data = res.json()
                response = data.get("response", "No response received.")
            else:
                response = f"Error {res.status_code}: {res.text}"
        except Exception as e:
            response = "Error: " + str(e)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
