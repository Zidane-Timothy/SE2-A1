from App.database import db
# from sqlalchemy import DateTime


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    date = db.Column(db.String(20), unique=False, nullable=False)
    location = db.Column(db.String(170), unique=False, nullable=False)
    entry_cost = db.Column(db.Float, unique=False, nullable=True)
    results = db.relationship('Result', backref='result', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, date, location, entry_cost):
        self.name = name
        self.date = date
        self.location = location
        self.entry_cost = entry_cost

    def __repr__(self):
        return f'<Competition: {self.id} | {self.name} at {self.location} on {self.date}>'
