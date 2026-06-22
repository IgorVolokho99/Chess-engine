from flask import Blueprint, session, redirect, url_for, current_app, render_template

from src.myapp.domain.errors.user_errors import UserNotFoundError

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect(url_for("auth.login_page"))

    use_cases = current_app.extensions["use_cases"]

    try:
        user = use_cases.get_current_user.execute(user_id)
    except UserNotFoundError:
        session.clear()
        return redirect(url_for("auth.login_page"))

    return render_template(
        "main/index.html",
        user=user,
    )
