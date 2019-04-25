from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team
from application.teams.forms import TeamForm

@app.route("/teams/new/")
@login_required(role="ADMIN")
def units_form():
    return render_template("teams/new.html", form = TeamForm())

#Unfinished