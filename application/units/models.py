from application import db
from application.models import Base

from sqlalchemy.sql import text

class Unit(Base):
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
    
    @staticmethod
    def number_of_units():
        stmt = text("SELECT COUNT(id) FROM Unit")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    #@staticmethod
    #def best_unit_in(stat):
        #stmt = text("SELECT name FROM Unit WHERE :stat = (SELECT MAX(:stat) FROM Unit)").params(stat=stat)
        #res = db.engine.execute(stmt)

        #for row in res:
            #return row[0]

    # I had to divide my original plan into seperate methods because calling above method several times in one render_template() caused "Too many positional arguments for staticmethod call" error.

    @staticmethod
    def best_unit_in_level():
        stmt = text("SELECT name FROM Unit WHERE level = (SELECT MAX(level) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_hp():
        stmt = text("SELECT name FROM Unit WHERE hp = (SELECT MAX(hp) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_strength():
        stmt = text("SELECT name FROM Unit WHERE strength = (SELECT MAX(strength) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_magic():
        stmt = text("SELECT name FROM Unit WHERE magic = (SELECT MAX(magic) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_skill():
        stmt = text("SELECT name FROM Unit WHERE skill = (SELECT MAX(skill) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_speed():
        stmt = text("SELECT name FROM Unit WHERE speed = (SELECT MAX(speed) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_luck():
        stmt = text("SELECT name FROM Unit WHERE luck = (SELECT MAX(luck) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_defense():
        stmt = text("SELECT name FROM Unit WHERE defense = (SELECT MAX(defense) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_resistance():
        stmt = text("SELECT name FROM Unit WHERE resistance = (SELECT MAX(resistance) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_movement():
        stmt = text("SELECT name FROM Unit WHERE movement = (SELECT MAX(movement) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_hpGrowth():
        stmt = text("SELECT name FROM Unit WHERE hpGrowth = (SELECT MAX(hpGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_strengthGrowth():
        stmt = text("SELECT name FROM Unit WHERE strengthGrowth = (SELECT MAX(strengthGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_magicGrowth():
        stmt = text("SELECT name FROM Unit WHERE magicGrowth = (SELECT MAX(magicGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_skillGrowth():
        stmt = text("SELECT name FROM Unit WHERE skillGrowth = (SELECT MAX(skillGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_speedGrowth():
        stmt = text("SELECT name FROM Unit WHERE speedGrowth = (SELECT MAX(speedGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_luckGrowth():
        stmt = text("SELECT name FROM Unit WHERE luckGrowth = (SELECT MAX(luckGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_defenseGrowth():
        stmt = text("SELECT name FROM Unit WHERE defenseGrowth = (SELECT MAX(defenseGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_resistanceGrowth():
        stmt = text("SELECT name FROM Unit WHERE resistanceGrowth = (SELECT MAX(resistanceGrowth) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

