from app import db
from datetime import datetime

class Machine(db.Model):
    __tablename__ = 'machines'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    def __repr__(self):
        return '<Machine %r>' % self.uuid

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(), unique=True, nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        default=datetime.utcnow)
    balance = db.Column(db.Integer, default=10)

    def __repr__(self):
        return '<Card %r>' % self.uuid


class Scan(db.Model):
    __tablename__ = 'scans'

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'),
                            nullable=False)
    machine = db.relationship('Machine',
                               backref=db.backref('scans', lazy=True))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'),
                           nullable=False)
    card = db.relationship('Card',
                               backref=db.backref('scans', lazy=True))

    amount = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, nullable=False,
                        default=datetime.utcnow)
    tag_on =db.Column(db.Boolean, default=True)