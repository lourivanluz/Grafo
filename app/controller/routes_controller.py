from http import HTTPStatus
from flask import request


from app.models.classes import Grafo

def search_router (graphId,town1,town2):


    try:
        town1 = str(town1).upper()
        town2 = str(town2).upper()

        if town1 == town2:
            return {'msg':"it's already at the end point"},HTTPStatus.OK
        connections = Grafo.get_connections_by_graphid(graph_id=graphId)
        if connections:
            args = request.args.get('maxStops')
            maxStops = int(args) if args else 0
            graph = Grafo(connections)
            routes = graph.search_deep_all_path(town1,town2,maxStops)

            response = [{"route":route,"stops":(len(route)-1)} for route in routes]
            return {'routes':response},HTTPStatus.OK
    
    except KeyError as e:
        return {"error": f"city '{e.args[0]}'not found in graph"}, HTTPStatus.BAD_REQUEST

    except Exception as e:
        return {"error": "internal server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

    
    