from url import db

class Message(db.Model):
    __tablename__ = 'messages'
    username = db.Column(db.String(15), index=True)
    message = db.Column(db.String(500), index=True)
