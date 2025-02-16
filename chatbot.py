from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello! Flask is running locally."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = f"You said: {user_message}"  # Replace with chatbot logic
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

