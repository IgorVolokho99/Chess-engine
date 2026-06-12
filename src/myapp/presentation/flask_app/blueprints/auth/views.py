from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for

from src.myapp.application.users.use_cases.register_user import RegisterUserCommand
from src.myapp.domain.errors.user_errors import UserAlreadyExistsError

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


@auth_bp.get("/register/success/<int:user_id>")
def register_success_page(user_id: int):
    return render_template(
        "auth/register_success.html",
        user_id=user_id,
    )
