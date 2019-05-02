from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base

from sqlalchemy.sql import text

class TeamUnit(Base):
    __table_args__ = (db.PrimaryKeyConstraint('team_id', 'unit_id'),)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    unit_id = db. Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)

    def __init__(self, team_id, unit_id):
        self.team_id = team_id
        self.unit_id = unit_id

class Team(Base):
    name = db.Column(db.String(144), nullable=False)

    units = db.relationship("TeamUnit", backref='unit', lazy=True, cascade="all, delete-orphan")
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name