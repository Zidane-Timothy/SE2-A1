import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import (create_user, get_all_users_json, get_all_users, initialize)
from App.controllers import (create_competition, get_user_competitions)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands')

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands')

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


app.cli.add_command(test)

'''
Competition commands
'''
competition = AppGroup("competition", help='Competition commands')

@competition.command("create_competition", help='Creates a user competition')
@click.argument("username", default="rob")
@click.argument("name", default="Code Runners")
@click.argument("date", default="01/01/1970")  # change to be actual datetime at some point
@click.argument("loc", default="Port of Spain")
@click.argument("cost", default="0.00")
def create_competition_command(username,  name, date, loc, cost):
    create_competition(username,  name, date, loc, cost)
    print(f'{name} created!')

@competition.command("list_user_competition", help='lists users competitions')
@click.argument("username", default="bob")
def list_user_competition_commands(username):
    print(get_user_competitions(username))


app.cli.add_command(competition) # add the group to the competitions cli
