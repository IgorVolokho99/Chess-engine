from flask import Flask, request, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)

USERS = {
    "admin": "123",
    "igor": "qwerty"
}
app.secret_key = "super-secret-key"


@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("game"))
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "login and password required"}), 400

    if login not in USERS or USERS[login] != password:
        return jsonify({"error": "invalid credentials"}), 401

    session["user"] = login

    return jsonify({"status": "OK"})


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    data = request.json

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "login and password required"}), 400

    if login in USERS:
        return jsonify({"error": "user already exists"}), 409

    USERS[login] = password
    session["user"] = login

    return jsonify({"status": "OK"})


@app.route("/game")
def game():
    if "user" not in session:
        return redirect(url_for("index"))
    return render_template("game.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
