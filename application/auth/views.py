from application import db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import createUser

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index")) 

@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/registerationform/")
def users_form():
    return render_template("auth/registerationform.html")

@app.route("/auth/", methods=["POST"])
def users_create():
    form = createUser(request.form)

    if not form.validate():
        return render_template("auth/registerationform.html", form = form)

    u = User(form.username.data, form.password.data, form.administrator.data)
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("units_index"))