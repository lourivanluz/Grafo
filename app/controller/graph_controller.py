from flask import jsonify, request
from http import HTTPStatus


from app.services import handle_data_graph

def create_graph():
    data:dict = request.get_json()
    result = handle_data_graph(**data)

    return jsonify(result),HTTPStatus.OK

def retriver_graph(graphId):
    return {'msg': graphId},HTTPStatus.OK   