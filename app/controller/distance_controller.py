from http import HTTPStatus


from app.models.classes import Grafo

def search_shortest_distance (graphId,town1,town2):
    if town1 == town2:
        return {'route':[{"distance":0,"path":[town1]}]},HTTPStatus.OK

    connections = Grafo.get_connections_by_graphid(graph_id=graphId)
    if connections:
        graph = Grafo(connections)
        routes = graph.search_deep_all_path(town1,town2)
        if not routes:
            return {'route':[{"distance":-1,"path":["no have path"]}]}

        routes_with_values:list[dict] = graph.calculate_route(routes)
        values_list = [list(route.values())[0] for route in routes_with_values]
        min_value = min(values_list)
        paths = [list(list(path.keys())[0]) for path in routes_with_values if list(path.values())[0] == min_value]
        result = [{"distance":min_value,"path":path} for path in paths]
        return {'routes':result},HTTPStatus.OK
        
    return {'error':'id not found'},HTTPStatus.NOT_FOUND