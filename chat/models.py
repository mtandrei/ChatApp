from chat import db

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    username = db.Column(db.String(15), index=True, nullable=False)
    message = db.Column(db.String(500), index=True, nullable=False)
