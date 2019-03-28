from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    administrator = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, administrator):
        self.username = username
        self.password = password
        self.administrator = administrator
        
  
    def get_id(self):
        return self.id

    def get_administrator(self):
        return self.administrator

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True