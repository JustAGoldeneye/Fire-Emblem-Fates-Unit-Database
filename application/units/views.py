from application import app, db
from flask import render_template, request
from application.units.models import Unit

@app.route("/units/new/")
def units_form():
    return render_template("units/new.html")

@app.route("/units/", methods=["POST"])
def units_create():
    u = Unit(request.form.get('name'))

    db.session().add(u)
    db.session().commit()

    return "hello world!"