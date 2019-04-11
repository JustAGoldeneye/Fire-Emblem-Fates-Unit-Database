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
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.level = (SELECT MAX(Unit.level) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_hp():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.hp = (SELECT MAX(Unit.hp) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_strength():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.strength = (SELECT MAX(Unit.strength) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_magic():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.magic = (SELECT MAX(Unit.magic) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_skill():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.skill = (SELECT MAX(Unit.skill) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_speed():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.speed = (SELECT MAX(Unit.speed) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_luck():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.luck = (SELECT MAX(Unit.luck) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_defense():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.defense = (SELECT MAX(Unit.defense) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_resistance():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.resistance = (SELECT MAX(Unit.resistance) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_movement():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.movement = (SELECT MAX(Unit.movement) FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_hpGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"hpGrowth\" = (SELECT MAX(Unit.\"hpGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_strengthGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"strengthGrowth\" = (SELECT MAX(Unit.\"strengthGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_magicGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"magicGrowth\" = (SELECT MAX(Unit.\"magicGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_skillGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"skillGrowth\" = (SELECT MAX(Unit.\"skillGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_speedGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"speedGrowth\" = (SELECT MAX(Unit.\"speedGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_luckGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"luckGrowth\" = (SELECT MAX(Unit.\"luckGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_defenseGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"defenseGrowth\" = (SELECT MAX(Unit.\"defenseGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def best_unit_in_resistanceGrowth():
        stmt = text("SELECT Unit.name FROM Unit WHERE Unit.\"resistanceGrowth\" = (SELECT MAX(Unit.\"resistanceGrowth\") FROM Unit)")
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

