from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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
