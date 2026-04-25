# Summative-Lab-v2---Flask-SQLAlchemy-Workout-Application-Backend

Description:
    This project is a Workout Application Backend built using Flask and SQLAlchemy. It allows users to track exercises, log workouts, and link specific exercises to those workouts with details like reps, sets, and duration. It follows a RESTful API architecture, ensuring that data is validated both at the database level and during JSON serialization.

Project Overview
    The application manages three main entities:
    Exercises: The catalog of movements (e.g., Pushups, Running).
    Workouts: The individual sessions recorded on a specific date.
    WorkoutExercises: A join table that connects Exercises to Workouts, storing specific performance metrics (Many-to-Many relationship).

Installation instructions (pipenv install)
    pipenv install
    pipenv shell

Required Packages(verify appropriate installation):
    werkzeug = "==2.2.2"
    importlib-metadata = "==6.0.0"
    importlib-resources = "==5.10.0"
    ipdb = "==0.13.9"
    marshmallow = "==3.20.1"
    flask-sqlalchemy = "*"
    sqlalchemy = "*"
    flask-migrate = "*"

Run Instructions:
    Flask db initiation:
        export FLASK_APP=server/app.py
        export PYTHONPATH=$PYTHONPATH:$(pwd)/server
        pipenv run flask db init
        pipenv run flask db migrate -m 'Initial migration: create tables'
        pipenv run flask db upgrade

Run seed file:
    PYTHONPATH=server pipenv run python server/seed.py

Run Flask server:
    pipenv run flask run --port 5555:

View Flask server in browser:
    Exercises:
        http://127.0.0.1:5555/exercises
    Workouts:
        http://127.0.0.1:5555/workouts

    
CRUD Commands in curl:
    CREATE(POST)
        Create new exercise(adjust exercise name and type as string, equipment as boolean):
            example command:
                curl -X POST http://127.0.0.1:5555/exercises \
                -H "Content-Type: application/json" \
                -d '{"name": "execise_name", "category": "exercise_type", "equipment_needed": true}'

        Create new workout(adjust date duration as integer, notes as string):
            example command:
                curl -X POST http://127.0.0.1:5555/workouts \
                -H "Content-Type: application/json" \
                -d '{"date": "2023-10-27T10:00:00", "duration_minutes": 60, "notes": "new_note"}'

        Add exercise to workout(adjust reps, sets, seconds as integers):
            example command:
                curl -X POST http://127.0.0.1:5555/workouts/1/exercises/1/workout_exercises \
                -H "Content-Type: application/json" \
                -d '{"reps": 12, "sets": 4, "duration_seconds": 0}'

    READ(GET)
        list all workouts:
            example command:
                curl http://127.0.0.1:5555/workouts

        Get specific exercise by ID:
            example command:
                curl http://127.0.0.1:5555/exercises/1
        
    DELETE(DELETE)
        delete a workout
            example command:
                curl -X DELETE http://127.0.0.1:5555/workouts/1

        Delete an Exercise:
            example command:
                curl -X DELETE http://127.0.0.1:5555/exercises/1