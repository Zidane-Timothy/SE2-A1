from App.models import Competition, Result, User
from App.database import db
import csv


def import_user_comp_results_csv(username, comp_name):
    user = User.query.filter_by(username=username)
    comp = Competition.query.filter_by(name=comp_name).first()

    if comp is None:
        print("competition does not exist")
        return

    results = Result.query.filter_by(comp_id=comp.id)

    res_file = input("Enter the results file name like this 'results.csv' ")
    with open(res_file, 'r') as res:
        reader = csv.DictReader(res)
        for line in reader:
            results = Result(compID=comp.id, name=line['participant_name'],
                             score=line['score'], rank=line['rank'],
                             category=line['category'],
                             notes=line['judges_comments'])
            # user.competitions.results.append(results)
            # print(user.competitions)
            db.session.add(results)
    db.session.commit()
    return


def list_competition_result(comp_name):
    comp = Competition.query.filter_by(name=comp_name).first()
    # result = Result.query.filter_by(comp_id=comp.id).first()
    result = Result.query.all()
    # print(result.id)

    if not result:
        print(f'could not find results for {comp_name}, try importing it first using that name')
        return

    return result
