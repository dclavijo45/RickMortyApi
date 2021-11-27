from util.Db import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    status = db.Column(db.String(7))
    species = db.Column(db.String(8))
    gender = db.Column(db.String(7))
    image = db.Column(db.String(30))

    def __init__(self, name, status, species, gender, image):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.image = image
