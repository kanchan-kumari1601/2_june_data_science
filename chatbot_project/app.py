from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Basic chatbot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm a bot, but I'm doing great!"
    elif "whatsup" in user_input or "what's up" in user_input:
        return "Not much! Just chatting with you 😊"

    elif "bye" in user_input:
        return "Goodbye! Talk to you later."
    else:
        return "I'm not sure how to respond to that."

@app.route("/")
def index():
    if "history" not in session:
        session["history"] = []
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    bot_reply = get_bot_response(user_message)

    session["history"].append(("You", user_message))
    session["history"].append(("Bot", bot_reply))

    return jsonify({"response": bot_reply, "history": session["history"]})

@app.route("/reset", methods=["POST"])
def reset():
    session["history"] = []
    return jsonify({"status": "reset", "history": session["history"]})

if __name__ == "__main__":
    app.run(debug=True)
