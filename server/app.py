import sys
import os
sys.path.append(os.getcwd() + '/server')
from flask import Flask,make_response, request
from flask_migrate import Migrate
from models import (
    db, Workout, workout_schema, workouts_schema, 
    Exercise, exercise_schema, exercises_schema,
    WorkoutExercise, workout_exercise_schema
)

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
        data = request.get_json()
        try:
            # Deserialization & Validation
            new_workout = workout_schema.load(data)
            workout = Workout(
                date=new_workout.get('date'),
                duration_minutes=new_workout.get('duration_minutes'),
                notes=new_workout.get('notes')
            )
            db.session.add(workout)
            db.session.commit()
            return make_response(workout_schema.dump(workout), 201)
        except Exception as e:
            return make_response({"errors": [str(e)]}, 400)
        

# GET /workouts/<id> & DELETE /workouts/<id>
@app.route('/workouts/<int:id>', methods=['GET', 'DELETE'])
def workout_by_id(id):
    workout = Workout.query.filter_by(id=id).first()
    if not workout:
        return make_response({"error": "Workout not found"}, 404)

    if request.method == 'GET':
        return make_response(workout_schema.dump(workout), 200)
    
    elif request.method == 'DELETE':
        db.session.delete(workout)
        db.session.commit()
        return make_response({}, 204)


# GET /exercises & POST /exercises
@app.route('/exercises', methods=['GET', 'POST'])
def exercises():
    if request.method == 'GET':
        exercises = Exercise.query.all()
        return make_response(exercises_schema.dump(exercises), 200)

    elif request.method == 'POST':
        data = request.get_json()
        try:
            new_ex = exercise_schema.load(data)
            exercise = Exercise(**new_ex)
            db.session.add(exercise)
            db.session.commit()
            return make_response(exercise_schema.dump(exercise), 201)
        except Exception as e:
            return make_response({"errors": [str(e)]}, 400)


# GET /exercises/<id> & DELETE /exercises/<id>
@app.route('/exercises/<int:id>', methods=['GET', 'DELETE'])
def exercise_by_id(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if not exercise:
        return make_response({"error": "Exercise not found"}, 404)

    if request.method == 'GET':
        return make_response(exercise_schema.dump(exercise), 200)

    elif request.method == 'DELETE':
        db.session.delete(exercise)
        db.session.commit()
        return make_response({}, 204)


# POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def create_workout_exercise(workout_id, exercise_id):
    data = request.get_json()
    try:
        new_we = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get('reps'),
            sets=data.get('sets'),
            duration_seconds=data.get('duration_seconds')
        )
        db.session.add(new_we)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(new_we), 201)
    except Exception as e:
        return make_response({"errors": [str(e)]}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)