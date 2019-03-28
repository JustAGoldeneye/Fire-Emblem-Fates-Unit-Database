from application import app, db
from flask import redirect, render_template, request, url_for
from application.units.models import Unit
from application.units.forms import UnitForm

@app.route("/units", methods=["GET"])
def units_index():
    return render_template("units/list.html", units = Unit.query.all())

@app.route("/units/new/")
def units_form():
    return render_template("units/new.html", form = UnitForm())

@app.route("/units/<unit_id>/", methods=["POST"])
def units_delete(unit_id):
    u = Unit.query.get(unit_id)

    db.session.delete(u)
    db.session.commit()

    return redirect(url_for("units_index"))

@app.route("/units/", methods=["POST"])
def units_create():
    u = Unit(request.form.get('name'), request.form.get('classGP'), request.form.get('level'), request.form.get('hp'), request.form.get('strength'), request.form.get('magic'), request.form.get('skill'), request.form.get('speed'), request.form.get('luck'), request.form.get('defense'), request.form.get('resistance'), request.form.get('movement'), request.form.get('hpGrowth'), request.form.get('strengthGrowth'), request.form.get('magicGrowth'), request.form.get('skillGrowth'), request.form.get('speedGrowth'), request.form.get('luckGrowth'), request.form.get('defenseGrowth'), request.form.get('resistanceGrowth'))

    if int(u.level) >= 1 and int(u.hp) >= 1 and int(u.strength) >= 0 and int(u.magic) >= 0 and int(u.skill) >= 0 and int(u.speed) >= 0 and int(u.luck) >= 0 and int(u.defense) >= 0 and int(u.resistance) >= 0 and int(u.movement) >= 0:
        db.session().add(u)
        db.session().commit()

    return redirect(url_for("units_index"))
