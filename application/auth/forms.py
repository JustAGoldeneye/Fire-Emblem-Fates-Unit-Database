from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, BooleanField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class createUser(FlaskForm):
    username = StringField("Username", [validators.Length(min=5)])
    password = StringField("Password", [validators.Length(min=5)])
    administrator = False

    class Meta:
        csrf = False

class createUserAdmin(FlaskForm):
    username = StringField("Username", [validators.Length(min=5)])
    password = StringField("Password", [validators.Length(min=5)])
    administrator = BooleanField("Give admin rights")

    class Meta:
        csrf = False
