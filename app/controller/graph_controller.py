from flask import jsonify, request
from http import HTTPStatus



from app.services import handle_data_graph
from app.models.classes import Grafo
from app.services.validate_body_services import verification_graphSechma

def create_graph():
    data:dict = request.get_json()
    validate = verification_graphSechma(data)
    if validate == 'valid filds':
        result = handle_data_graph(**data)
        return jsonify(result[0]),result[1]
    return {'error':validate},HTTPStatus.BAD_REQUEST

def retriver_graph(graphId):
        connection_list = Grafo.get_connections_by_graphid(graph_id=graphId)
        if connection_list:
            return {'id':graphId,'data':connection_list},HTTPStatus.OK

        return {'error':'id not found'},HTTPStatus.NOT_FOUND

      