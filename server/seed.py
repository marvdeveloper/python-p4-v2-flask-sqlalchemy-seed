#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    # Initialize faker
    fake = Faker()

    # Delete all rows from the pets table
    Pet.query.delete()

    # Define possible species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Create 10 random pets
    pets = []
    for _ in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert and commit
    db.session.add_all(pets)
    db.session.commit()
