from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    login = data.get("login")
    password = data.get("password")

    print(login)
    print(password)

    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(debug=True)
