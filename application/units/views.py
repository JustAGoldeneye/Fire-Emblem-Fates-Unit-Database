from application import app, db
from flask import redirect, render_template, request, url_for
from application.units.models import Unit

@app.route("/units", methods=["GET"])
def units_index():
    return render_template("units/list.html", units = Unit.query.all())

@app.route("/units/new/")
def units_form():
    return render_template("units/new.html")

@app.route("/units/", methods=["POST"])
def units_create():
    u = Unit(request.form.get('name'), request.form.get('classGP'), request.form.get('level'), request.form.get('hp'), request.form.get('strength'), request.form.get('magic'), request.form.get('skill'), request.form.get('speed'), request.form.get('luck'), request.form.get('defense'), request.form.get('resistance'), request.form.get('movement'), request.form.get('hpGrowth'), request.form.get('strengthGrowth'), request.form.get('magicGrowth'), request.form.get('skillGrowth'), request.form.get('speedGrowth'), request.form.get('luckGrowth'), request.form.get('defenseGrowth'), request.form.get('resistanceGrowth'))

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("units_index"))