from flask.views import MethodView
from flask import jsonify, request

class ApiRickAndMortyController(MethodView):
    def get(self):
        return jsonify({'message': 'ok'}), 200

    def post(self):
        json_request = request.get_json(force=True)
        return jsonify({'message': 'ok'}), 200

    def put(self):
        json_request = request.get_json(force=True)
        return jsonify({'message': 'ok'}), 200

    def delete(self):
        json_request = request.get_json(force=True)
        return jsonify({'message': 'ok'}), 200
