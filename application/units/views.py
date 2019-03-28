from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.units.models import Unit
from application.units.forms import UnitForm

@app.route("/units", methods=["GET"])
@login_required
def units_index():
    return render_template("units/list.html", units = Unit.query.all())

@app.route("/units/new/")
@login_required
def units_form():
    return render_template("units/new.html", form = UnitForm())

@app.route("/units/<unit_id>/", methods=["POST"])
@login_required
def units_delete(unit_id):
    u = Unit.query.get(unit_id)

    db.session.delete(u)
    db.session.commit()

    return redirect(url_for("units_index"))

@app.route("/units/", methods=["POST"])
@login_required
def units_create():
    form = UnitForm(request.form)

    if not form.validate():
        return render_template("units/new.html", form = form)

    u = Unit(form.name.data, form.classGP.data, form.level.data, form.hp.data, form.strength.data, form.magic.data, form.skill.data, form.speed.data, form.luck.data, form.defense.data, form.resistance.data, form.movement.data, form.hpGrowth.data, form.strengthGrowth.data, form.magicGrowth.data, form.skillGrowth.data, form.speedGrowth.data, form.luckGrowth.data, form.defenseGrowth.data, form.resistanceGrowth.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("units_index"))
