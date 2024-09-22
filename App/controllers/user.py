from App.models import User, Competition
from App.database import db
from App.models import competition

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None


# to be edited to accpet team names in the future
def create_competition(username, name, date, loc, cost):
    user = User.query.filter_by(username=username).first()
    if not user:
        print(f'{username} not found')
        return

    new_competition = Competition(name, date, loc, cost)
    user.competitions.append(new_competition)
    db.session.add(user)
    db.session.commit()


def get_user_competitions(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        # insert try here
        print(f'{username} not found!')
        return
    print(user.competitions)

# def get_user_competitions_json(username):
#     return

# def import_user_comp_csv():
#     with open()
