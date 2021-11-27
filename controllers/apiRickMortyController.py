from services.apiService import ApiService
from flask.views import MethodView
from flask import jsonify, request

class ApiRickAndMortyController(MethodView):
    def get(self, id=None):
        service = ApiService()

        if id:
            data = service.get(id)
        else:
            data = service.getAll()

        return jsonify(data), 200

    def post(self):
        json_request = request.get_json()
        service = ApiService()

        try:
            name = json_request['name']
            status = json_request['status']
            species = json_request['species']
            gender = json_request['gender']
            image = json_request['image']
            result = service.create(name, status, species, gender, image)
        except Exception as e:
            print(str(e))
            return jsonify({'saved': False}), 400

        return jsonify({'saved': result}), 200

    def put(self, id=None):
        json_request = request.get_json()
        service = ApiService()

        if not id:
            return jsonify({'saved': False}), 400

        try:
            name = json_request['name']
            status = json_request['status']
            species = json_request['species']
            gender = json_request['gender']
            image = json_request['image']
            result = service.update(id, name, status, species, gender, image)
        except Exception as e:
            print(str(e))
            return jsonify({'updated': False}), 400

        return jsonify({'updated': result}), 200

    def delete(self, id=None):
        if not id:
            return jsonify({'deleted': False}), 400

        try:
            service = ApiService()

            result = service.delete(id)
        except Exception as e:
            print(e)
            return jsonify({'deleted': False}), 400

        return jsonify({'deleted': result}), 200
