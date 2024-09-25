from App.database import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'),
                        nullable=False)

    participant_name = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(15), nullable=False)
    notes = db.Column(db.String(200), nullable=False)

    def __init__(self, compID, name, score, rank, category, notes):
        self.comp_id = compID
        self.participant_name = name
        self.score = score
        self.rank = rank
        self.category = category
        self.notes = notes

    def __repr__(self):
        return f'<Results: \n{self.id} | {self.participant_name} Score: {self.score} with rank {self.rank} Category:{self.category}. Judges Comments: {self.notes}>'
