from App.models import Competition, Result, User
from App.database import db
import csv


def get_competition(id):
    return Competition.query.get(id)


def get_all_competitions():
    return Competition.query.all()


def import_user_comp_results_csv(username, comp_name):
    user = User.query.filter_by(username=username).first()
    if not user:
        print(f'{username} not found!')
        return

    comp = Competition.query.filter_by(name=comp_name, user_id=user.id).first()

    if comp is None:
        print("competition does not exist")
        return

    print(comp)

    res_file = input("Enter the results file name like this 'results.csv' ")
    with open(res_file, 'r') as res:
        reader = csv.DictReader(res)
        for line in reader:
            result_row = Result(compID=comp.id, name=line['participant_name'],
                             score=line['score'], rank=line['rank'],
                             category=line['category'],
                             notes=line['judges_comments'])

            db.session.add(result_row)
            comp.results.append(result_row)
    db.session.commit()
    return


def list_competition_result(comp_name):
    comp = Competition.query.filter_by(name=comp_name).first()

    if not comp:

        print(f'could not find results for {comp_name}, try importing it first using that name')
        return

    for res in comp.results:
        print(f'\nID: {res.id}, Name: {res.participant_name}, Rank: {res.rank}, Score:{res.score} \nJudges Notes: {res.notes}')
