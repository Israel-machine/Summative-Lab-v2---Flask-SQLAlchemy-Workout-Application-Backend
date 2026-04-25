from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, default=False)
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')
    workouts = db.relationship('Workout', secondary='workout_exercises', viewonly=True)

    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name) < 1:
            raise ValueError("Exercise must have a name.")
        return name

    def __repr__(self):
        return f'<Exercise {self.name}, Category: {self.category}>'
    

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)
    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
    exercises = db.relationship('Exercise', secondary='workout_exercises', viewonly=True)
    @validates('duration_minutes')
    def validate_duration(self, key, duration):
        if duration <= 0:
            raise ValueError("Duration must be greater than 0 minutes.")
        return duration

    def __repr__(self):
        return f'<Workout ID: {self.id}, Date: {self.date}>'
    

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)
    
    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')
    @validates('reps')
    def validate_reps(self, key, reps):
        if reps < 0:
            raise ValueError("Reps cannot be negative.")
        return reps

    def __repr__(self):
        return f'<WorkoutExercise Workout: {self.workout_id}, Exercise: {self.exercise_id}>'