from App.database import db
from datetime import datetime


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    location = db.column(db.String(170), unique=False, nullable=False)
    entry_cost = db.Column(db.Float, unique=False, nullable=False)

    def __init__(self, name, date, location, entry_cost):
        self.name = name
        self.date = date
        self.location = location
        self.entry_cost = entry_cost

    def __repr__(self):
        return f'<Competition: {self.name} | {self.location}>'
