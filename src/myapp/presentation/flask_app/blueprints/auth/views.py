"""Module that contains auth views."""

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from src.myapp.application.users.use_cases.login_user import LoginUserCommand
from src.myapp.application.users.use_cases.register_user import RegisterUserCommand
from src.myapp.domain.errors.user_errors import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
)

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.get("/register")
def register_page() -> None:
    """View for presentation registration page."""
    return render_template("auth/register.html")


@auth_bp.post("/register")
def register_action() -> None:
    """View for user registration.

    If user gives invalid data(used e-mail) redirect to register page.
    If user gives valid data redirect to main page.
    """
    command = RegisterUserCommand(
        user_name=request.form["user_name"],
        email=request.form["email"],
        password=request.form["password"],
    )

    use_cases = current_app.extensions["use_cases"]

    try:
        user_id = use_cases.register_user.execute(command)
    except UserAlreadyExistsError:
        flash("User with this email already exists.")
        return redirect(url_for("auth.register_page"))

    return redirect(url_for("main.index", user_id=user_id))


@auth_bp.get("/login")
def login_page() -> None:
    """View for presentation log in page."""
    return render_template("auth/login.html")


@auth_bp.post("/login")
def login_action() -> None:
    """View for log in of user.

    If user gives invalid credentials redirect to login page.
    If user gives valid credentials clear current session and
    save new data into session.
    """
    command = LoginUserCommand(
        user_name=request.form["user_name"],
        password=request.form["password"],
    )

    use_cases = current_app.extensions["use_cases"]

    try:
        user_id = use_cases.login_user.execute(command)
    except InvalidCredentialsError as err:
        flash(str(err))
        return redirect(url_for("auth.login_page"))

    session.clear()
    session["user_id"] = user_id

    return redirect(url_for("main.index"))


@auth_bp.get("/profile")
def profile_page() -> None:
    """View for profile of user.

    If user id equals None redirects to login page.
    """
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("auth.login_page"))

    return f"Logged in as user #{user_id}"


@auth_bp.post("/logout")
def logout_action() -> None:
    """View for logout.

    Clears session and redirects to login page.
    """
    session.clear()

    return redirect(url_for("auth.login_page"))
