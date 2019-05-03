from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team, TeamUnit
from application.teams.forms import TeamForm, AddUnitForm
from application.units.models import Unit

@app.route("/teams", methods=["GET"])
@login_required(role="ADMIN")
def teams_index():
    return render_template("teams/list.html", teams = Team.find_users_teams(current_user.id), form = TeamForm(), units = Team.units_in_teams(current_user.id), unit_numbers = Team.number_of_units_in_teams(current_user.id))

@app.route("/teams/show/<team_id>/", methods=["GET"])
@login_required(role="ADMIN")
def teams_show(team_id):
    return render_template("teams/show.html", team_id = team_id, team = Team.find_team(team_id), units = Team.get_units_in_team(team_id), number_of_units = Team.number_of_units_in_team(team_id), form = AddUnitForm())

@app.route("/teams/", methods=["POST"])
@login_required(role="ADMIN")
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/list.html", teams = Team.find_users_teams(current_user.id), units = Team.units_in_teams(current_user.id), unit_numbers = Team.number_of_units_in_teams(current_user.id), form = form)

    t  = Team(form.name.data)
    t.account_id = current_user.id

    db.session.add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/<team_id>/", methods=['GET','POST'])
@login_required(role="ADMIN")
def teams_delete(team_id):
    t = Team.query.get(team_id)

    db.session.delete(t)
    db.session.commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/show/<team_id>", methods=['GET','POST'])
@login_required(role="ADMIN")
def teams_add_unit(team_id):
    form = AddUnitForm(request.form)

    if not form.validate():
        return render_template("teams/show.html", form = form, number_of_units = Team.number_of_units_in_team(team_id), team = Team.find_team(team_id))

    unit_name = form.name.data
    unit_ids = Unit.get_unit_ids_with_name(unit_name)
    
    if unit_ids:
        tu = TeamUnit(team_id = team_id, unit_id = unit_ids[0])
        db.session.add(tu)
        db.session.commit()

    return redirect(url_for("teams_index"))