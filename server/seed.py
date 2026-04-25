#!/usr/bin/env python3
import sys
import os
sys.path.append(os.getcwd() + '/server')
from datetime import datetime
from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():
    print("Clearing database...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    e1 = Exercise(name="Pushups", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="Cardio", equipment_needed=False)
    e3 = Exercise(name="Bench Press", category="Strength", equipment_needed=True)
    db.session.add_all([e1, e2, e3])

    print("Seeding workouts...")
    w1 = Workout(date=datetime.now(), duration_minutes=45, notes="Morning session")
    w2 = Workout(date=datetime.now(), duration_minutes=30, notes="Quick cardio")
    db.session.add_all([w1, w2])
    db.session.commit() # Commit parents first to get IDs

    print("Seeding join table...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, reps=20, sets=3)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id, duration_seconds=1800)
    db.session.add_all([we1, we2])
    
    db.session.commit()
    print("Seeding complete!")