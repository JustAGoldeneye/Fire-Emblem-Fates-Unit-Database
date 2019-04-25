from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base

from sqlalchemy.sql import text 

class Team(Base):
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

class UnitTeam(Base):
    unit_id = db.Column(Integer, ForeignKey('unit.id'))
    team_id = db.Column(Integer, ForeignKey('team.id'))

    unit = relationship('User', backref=db.backref('account'))
    team = relationship('Team', backref=db.backref('team'))
    