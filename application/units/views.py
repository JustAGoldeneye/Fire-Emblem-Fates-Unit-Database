from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.units.models import Unit
from application.units.forms import UnitForm

@app.route("/units", methods=["GET"])
def units_index():
    return render_template("units/list.html", units = Unit.query.all(), number_of_units=Unit.number_of_units(), best_unit_in_level=Unit.best_unit_in_level(), best_unit_in_hp= Unit.best_unit_in_hp(), best_unit_in_strength=Unit.best_unit_in_strength(), best_unit_in_magic=Unit.best_unit_in_magic(), best_unit_in_skill=Unit.best_unit_in_skill(), best_unit_in_speed=Unit.best_unit_in_speed(), best_unit_in_luck=Unit.best_unit_in_luck(), best_unit_in_defense=Unit.best_unit_in_defense(), best_unit_in_resistance=Unit.best_unit_in_resistance(), best_unit_in_movement=Unit.best_unit_in_movement(), best_unit_in_hpGrowth= Unit.best_unit_in_hpGrowth(), best_unit_in_strengthGrowth=Unit.best_unit_in_strengthGrowth(), best_unit_in_magicGrowth=Unit.best_unit_in_magicGrowth(), best_unit_in_skillGrowth=Unit.best_unit_in_skillGrowth(), best_unit_in_speedGrowth=Unit.best_unit_in_speedGrowth(), best_unit_in_luckGrowth=Unit.best_unit_in_luckGrowth(), best_unit_in_defenseGrowth=Unit.best_unit_in_defenseGrowth(), best_unit_in_resistanceGrowth=Unit.best_unit_in_resistanceGrowth())

@app.route("/units/new/")
@login_required(role="ADMIN")
def units_form():
    return render_template("units/new.html", form = UnitForm())

@app.route("/units/edit/<unit_id>/", methods=["GET"])
@login_required(role="ADMIN")
def units_editForm(unit_id):
    return render_template("units/edit.html", units = Unit.query.filter_by(id=unit_id), form = UnitForm())

@app.route("/units/<unit_id>/", methods=['GET','POST'])
@login_required(role="ADMIN")
def units_delete(unit_id):
    u = Unit.query.get(unit_id)

    db.session.delete(u)
    db.session.commit()

    return redirect(url_for("units_index"))

@app.route("/units/", methods=["POST"])
@login_required(role="ADMIN")
def units_create():
    form = UnitForm(request.form)

    if not form.validate():
        return render_template("units/new.html", form = form)

    u = Unit(form.name.data, form.classGP.data, form.level.data, form.hp.data, form.strength.data, form.magic.data, form.skill.data, form.speed.data, form.luck.data, form.defense.data, form.resistance.data, form.movement.data, form.hpGrowth.data, form.strengthGrowth.data, form.magicGrowth.data, form.skillGrowth.data, form.speedGrowth.data, form.luckGrowth.data, form.defenseGrowth.data, form.resistanceGrowth.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("units_index"))

@app.route("/units/<unit_id>/", methods=['GET','POST'])
@login_required(role="ADMIN")
def units_edit(unit_id):

    #u = Unit.query.get(unit_id)
    
    #form = UnitForm(request.form)

    #if not form.validate():
        #return render_template("units/edit.html", form = form)

    #u.name = request.form.get('name')
    #u.classGP = request.form.get('classGP')
    #u.level = request.form.get('level')
    #u.hp = request.form.get('hp')
    #u.strength = request.form.get('strength')
    #u.magic = request.form.get('magic')
    #u.skill = request.form.get('skill')
    #u.speed = request.form.get('speed')
    #u.luck = request.form.get('luck')
    #u.defense = request.form.get('defense')
    #u.resistance = request.form.get('resistance')
    #u.movement = request.form.get('movement')
    #u.hpGrowth = request.form.get('hpGrowth')
    #u.strengthGrowth = request.form.get('strengthGrowth')
    #u.magicGrowth = request.form.get('magicGrowth')
    #u.skillGrowth = request.form.get('skillGrowth')
    #u.speedGrowth = request.form.get('speedGrowth')
    #u.luckGrowth = request.form.get('luckGrowth')
    #u.defenseGrowth = request.form.get('defenseGrowth')
    #u.resistanceGrowth = request.form.get('resistanceGrowth')

    #This method always deletes the row in the database, even with just commit and final return. (units_delete doesn't)

    db.session().commit()
    
    return redirect(url_for("units_index"))
