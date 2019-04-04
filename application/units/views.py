from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.units.models import Unit
from application.units.forms import UnitForm

@app.route("/units", methods=["GET"])
@login_required
def units_index():
    return render_template("units/list.html", units = Unit.query.all(), number_of_units=Unit.number_of_units())

@app.route("/units/new/")
@login_required
def units_form():
    return render_template("units/new.html", form = UnitForm())

@app.route("/units/edit/", methods=["GET"])
@login_required
def units_editForm():
    return render_template("units/edit.html", units = Unit.query.filter_by(id=2), form = UnitForm()) # muokkaa

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

@app.route("/units/<unit_id>/", methods=["POST"])
@login_required
def units_edit(unit_id):
    form = UnitForm(request.form)

    if not form.validate():
        return render_template("units/edit.html", form = form)

    u = Unit.query.get(unit_id)

    u.name = request.form.get('name')
    u.classGP = request.form.get('classGP')
    u.level = request.form.get('level')
    u.hp = request.form.get('hp')
    u.strength = request.form.get('strength')
    u.magic = request.form.get('magic')
    u.skill = request.form.get('skill')
    u.speed = request.form.get('speed')
    u.luck = request.form.get('luck')
    u.defense = request.form.get('defense')
    u.resistance = request.form.get('resistance')
    u.movement = request.form.get('movement')
    u.hpGrowth = request.form.get('hpGrowth')
    u.strengthGrowth = request.form.get('strengthGrowth')
    u.magicGrowth = request.form.get('magicGrowth')
    u.skillGrowth = request.form.get('skillGrowth')
    u.speedGrowth = request.form.get('speedGrowth')
    u.luckGrowth = request.form.get('luckGrowth')
    u.defenseGrowth = request.form.get('defenseGrowth')
    u.resistanceGrowth = request.form.get('resistanceGrowth')

    db.session().commit()
    
    return redirect(url_for("units_index"))
