from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class UnitForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=1)])
    classGP = StringField("Class", [validators.Length(min=1)])
    level = IntegerField("Level", [validators.NumberRange(min=1)])
    hp = IntegerField("HP", [validators.NumberRange(min=1)])
    strength = IntegerField("Strength", [validators.NumberRange(min=0)])
    magic = IntegerField("Magic", [validators.NumberRange(min=0)])
    skill = IntegerField("Skill", [validators.NumberRange(min=0)])
    speed = IntegerField("Speed", [validators.NumberRange(min=0)])
    luck = IntegerField("Luck", [validators.NumberRange(min=0)])
    defense = IntegerField("Defense", [validators.NumberRange(min=0)])
    resistance = IntegerField("Resistance", [validators.NumberRange(min=0)])
    movement = IntegerField("Movement", [validators.NumberRange(min=0)])
    hpGrowth = IntegerField("HP Growth %", [validators.NumberRange(min=0)])
    strengthGrowth = IntegerField("Strength Growth %", [validators.NumberRange(min=0)])
    magicGrowth = IntegerField("Magic Growth %", [validators.NumberRange(min=0)])
    skillGrowth = IntegerField("Skill Growth %", [validators.NumberRange(min=0)])
    speedGrowth = IntegerField("Speed Growth %", [validators.NumberRange(min=0)])
    luckGrowth = IntegerField("Luck Growth %", [validators.NumberRange(min=0)])
    defenseGrowth = IntegerField("Defense Growth %", [validators.NumberRange(min=0)])
    resistanceGrowth = IntegerField("Resistance Growth %", [validators.NumberRange(min=0)])

    class Meta:
        csrf = False
