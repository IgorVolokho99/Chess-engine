"""Defain routes for rendering the application's main page."""

from flask import Blueprint, current_app, redirect, render_template, session, url_for

from src.myapp.domain.errors.user_errors import UserNotFoundError

main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def index() -> None:
    """Render the main page for the authenticated user.

    Redirects unauthenticated users to the login page. If ther user stored
    in the session no longer exists, clears the session and redirects to the
    login page.
    """
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
