from chatapi import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # sent_msgs = db.relationship('Message', backref='sender', lazy=True)
    # received_msgs = db.relationship('Message', backref='recipient', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_type = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Text(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)
    text = db.Column(db.String(60), nullable=False)


class Image(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)
    url = db.Column(db.String(60), nullable=False)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)


class Video(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)
    url = db.Column(db.String(60), nullable=False)
    source = db.Column(db.String(60))
