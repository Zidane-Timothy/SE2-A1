from App.models import Student, Competition
from App.database import db
from sqlalchemy.exc import IntegrityError


def create_user(username, email, password):
    newuser = Student(username=username, email=email, password=password)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Username or email already exist")
    else:
        return newuser


def get_user_by_username(username):
    return Student.query.filter_by(username=username).first()


def get_user(id):
    return Student.query.get(id)


def get_all_users():
    return Student.query.all()


def get_all_users_json():
    users = Student.query.all()
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
    student = Student.query.filter_by(username=username).first()
    print(student)
    if student is not None:
        new_competition = Competition(name, date, loc, cost)
        student.competitions.append(new_competition)
        db.session.add(new_competition)
        db.session.commit()
        return new_competition
    else:
        print(f'{username} not found')
        return None


def get_user_competitions(username):
    student = Student.query.filter_by(username=username).first()
    if not student:
        # insert try here
        print(f'{username} not found!')
        return
    print(student.competitions)
