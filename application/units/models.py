from application import db

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    classGP = db.Column(db.String(144), nullable=False) #GP = gameplay, The name is meant to reduce ambiguity between game terms and programming terms.
    level = db.Column(db.Integer, nullable=False)

    hp = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    magic = db.Column(db.Integer, nullable=False)
    skill = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    luck = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    resistance = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.Integer, nullable=False)

    hpGrowth = db.Column(db.Integer, nullable=False)
    strengthGrowth = db.Column(db.Integer, nullable=False)
    magicGrowth = db.Column(db.Integer, nullable=False)
    skillGrowth = db.Column(db.Integer, nullable=False)
    speedGrowth = db.Column(db.Integer, nullable=False)
    luckGrowth = db.Column(db.Integer, nullable=False)
    defenseGrowth = db.Column(db.Integer, nullable=False)
    resistanceGrowth = db.Column(db.Integer, nullable=False)

    def __init__(self, name, classGP, level, hp, strength, magic, skill, speed, luck, defense, resistance, movement, hpGrowth, strengthGrowth, magicGrowth, skillGrowth, speedGrowth, luckGrowth, defenseGrowth, resistanceGrowth):
        self.name = name
        self.classGP = classGP
        self.level = level

        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.skill = skill
        self.speed = speed
        self.luck = luck
        self.defense = defense
        self.resistance = resistance
        self.movement = movement

        self.hpGrowth = hpGrowth
        self.strengthGrowth = strengthGrowth
        self.magicGrowth = magicGrowth
        self.skillGrowth = skillGrowth
        self.speedGrowth = speedGrowth
        self.luckGrowth = luckGrowth
        self.defenseGrowth = defenseGrowth
        self.resistanceGrowth = resistanceGrowth
