# Summative-Lab-v2---Flask-SQLAlchemy-Workout-Application-Backend

Flask db initiation:
export FLASK_APP=server/app.py
export PYTHONPATH=$PYTHONPATH:$(pwd)/server

pipenv run flask db init
pipenv run flask db migrate -m 'Initial migration: create tables'
pipenv run flask db upgrade

run seed file:
PYTHONPATH=server pipenv run python server/seed.py