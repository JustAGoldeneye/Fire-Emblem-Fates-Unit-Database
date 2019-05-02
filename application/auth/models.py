from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    teams = db.relationship("Team", backref="account", lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self): #unfinished
        return ["ADMIN"]

    def is_admin(self): #unfinished
        return True