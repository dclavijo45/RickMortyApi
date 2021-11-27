from schemas.CharacterSchema import characters, character
from models.Character import Character
from util.Db import db

class ApiService:
    def getAll(self):
        try:
            result = Character.query.all()

            return characters.dump(result)
        except Exception as e:
            print(e)
            return {}
    
    def get(self, id):
        try:
            result = Character.query.get(id)

            return character.dump(result)
        except Exception as e:
            print(e)
            return {}

    def create(self, name, status, species, gender, image):
        try:
            new_character = Character(name, status, species, gender, image)
            db.session.add(new_character)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def update(self, id, name, status, species, gender, image):
        try:
            result = Character.query.get(id)

            result.name = name
            result.status = status
            result.species = species
            result.gender = gender
            result.image = image
            
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id):
        try:
            result = Character.query.get(id)
            db.session.delete(result)
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False