from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class UnitForm(FlaskForm):
    name = StringField("Name")
    classGP = StringField("Class")
    level = IntegerField("Level")
    hp = IntegerField("HP")
    strength = IntegerField("Strength")
    magic = IntegerField("Magic")
    skill = IntegerField("Skill")
    speed = IntegerField("Speed")
    luck = IntegerField("Luck")
    defense = IntegerField("Defense")
    resistance = IntegerField("Resistance")
    movement = IntegerField("Movement")
    hpGrowth = IntegerField("HP Growth %")
    strengthGrowth = IntegerField("Strength Growth %")
    magicGrowth = IntegerField("Magic Growth %")
    skillGrowth = IntegerField("Skill Growth %")
    speedGrowth = IntegerField("Speed Growth %")
    luckGrowth = IntegerField("Luck Growth %")
    defenseGrowth = IntegerField("Defense Growth %")
    resistanceGrowth = IntegerField("Resistance Growth %")

    class Meta:
        csrf = False
