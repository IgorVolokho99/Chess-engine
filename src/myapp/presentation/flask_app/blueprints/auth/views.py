from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for, session

from src.myapp.application.users.use_cases.login_user import LoginUserCommand
from src.myapp.application.users.use_cases.register_user import RegisterUserCommand
from src.myapp.domain.errors.user_errors import UserAlreadyExistsError, InvalidCredentialsError

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.get("/register")
def register_page():
    return render_template("auth/register.html")


@auth_bp.post("/register")
def register_action():
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

    return redirect(url_for("auth.register_success_page", user_id=user_id))


@auth_bp.get("/login")
def login_page():
    return render_template("auth/login.html")


@auth_bp.post("/login")
def login_action():
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

    return redirect(url_for("auth.profile_page"))


@auth_bp.get("/profile")
def profile_page():
    user_id = session.get("user_id")

    if user_id is None:
        return redirect(url_for("auth.login_page"))

    return f"Logged in as user #{user_id}"


@auth_bp.post("/logout")
def logout_action():
    session.clear()

    return redirect(url_for("auth.login_page"))


@auth_bp.get("/register/success/<int:user_id>")
def register_success_page(user_id: int):
    return render_template(
        "auth/register_success.html",
        user_id=user_id,
    )
