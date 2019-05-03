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
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_users_teams(account_id):
        stmt = text("SELECT * FROM team "
                    "WHERE account_id = :accountid")

        res = db.engine.execute(stmt, accountid = account_id)
        result = []
        for row in res:
            result.append(row)

        return result

    @staticmethod
    def find_team(team_id):
        stmt = text("SELECT * FROM team "
                    "WHERE id = :teamid")

        res = db.engine.execute(stmt, teamid = team_id)

        for row in res:
            return row

    @staticmethod
    def number_of_units_in_team(team_id):
        stmt = text("SELECT COUNT(team.id) FROM team "
                    "JOIN team_unit ON team.id = team_unit.team_id "
                    "JOIN unit ON team_unit.team_id = unit.id "
                    "WHERE team.id = :teamid")

        res = db.engine.execute(stmt, teamid = team_id)

        for row in res:
            return row[0]
