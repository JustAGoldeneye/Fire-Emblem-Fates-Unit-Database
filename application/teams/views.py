from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team
from application.teams.forms import TeamForm

@app.route("/teams", methods=["GET"])
@login_required(role="ADMIN")
def teams_index():
    return render_template("teams/list.html", teams = Team.find_users_teams(current_user.id), form = TeamForm())

@app.route("/teams/", methods=["POST"])
@login_required(role="ADMIN")
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/list.html", form = form)

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
