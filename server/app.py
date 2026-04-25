import sys
import os
sys.path.append(os.getcwd() + '/server')
from flask import Flask,make_response, request
from flask_migrate import Migrate
from models import db, Workout, WorkoutExercise, Exercise, workouts_schema, workout_schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
# GET /workouts & POST /workouts
@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if request.method == 'GET':
        workouts = Workout.query.all()
        return make_response(workouts_schema.dump(workouts), 200)
    elif request.method == 'POST':
        return make_response({"message": "Create workout placeholder"}, 201)

# GET /workouts/<id> & DELETE /workouts/<id>
@app.route('/workouts/<int:id>', methods=['GET', 'DELETE'])
def workout_by_id(id):
    if request.method == 'GET':
        return make_response({"message": f"Show workout {id} placeholder"}, 200)
    elif request.method == 'DELETE':
        return make_response({"message": f"Delete workout {id} placeholder"}, 204)

# GET /exercises & POST /exercises
@app.route('/exercises', methods=['GET', 'POST'])
def exercises():
    if request.method == 'GET':
        return make_response({"message": "List of all exercises placeholder"}, 200)
    elif request.method == 'POST':
        return make_response({"message": "Create exercise placeholder"}, 201)

# GET /exercises/<id> & DELETE /exercises/<id>
@app.route('/exercises/<int:id>', methods=['GET', 'DELETE'])
def exercise_by_id(id):
    if request.method == 'GET':
        return make_response({"message": f"Show exercise {id} placeholder"}, 200)
    elif request.method == 'DELETE':
        return make_response({"message": f"Delete exercise {id} placeholder"}, 204)

# POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def create_workout_exercise(workout_id, exercise_id):
    return make_response({"message": f"Add exercise {exercise_id} to workout {workout_id} placeholder"}, 201)

if __name__ == '__main__':
    app.run(port=5555, debug=True)