from flask import jsonify, request
from http import HTTPStatus



from app.services import handle_data_graph
from app.models.classes import Grafo

def create_graph():
    data:dict = request.get_json()
    result = handle_data_graph(**data)

    return jsonify(result),HTTPStatus.OK

def retriver_graph(graphId):
        connection_list = Grafo.get_connections_by_graphid(graph_id=graphId)
        if connection_list:
            return {'id':graphId,'data':connection_list},HTTPStatus.OK
            
        return {'error':'id not found'},HTTPStatus.NOT_FOUND

      