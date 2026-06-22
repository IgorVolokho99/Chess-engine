from flask import Blueprint, session, redirect, url_for

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect(url_for("auth.login_page"))

    return f"You are authenticated. Your user id: {user_id}"
