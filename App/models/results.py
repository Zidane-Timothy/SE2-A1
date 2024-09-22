from App.database import db


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)  # teamName
    placing = db.Column(db.String(5))
    reward = db.Column(db.String(50), nullable=True)

    def __init__(self, userID, compID, name):
        self.user_id = userID
        self.comp_id = compID
        self.name = name
