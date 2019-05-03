from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])

    class Meta:
        csrf = False

class AddUnitForm(FlaskForm):
    name = StringField("Name")