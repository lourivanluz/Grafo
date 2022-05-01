from app.models.classes import Grafo

def handle_data_graph(**data):
    noh_list = data.get('data')
    graph = Grafo(noh_list)
    if(graph.validate):
        saved_graph = graph.save_in_db()
        serializer = Grafo.get_connections_by_graphid(graph_id=saved_graph.graph_id)

        return {'id':saved_graph.graph_id,'data':serializer}

    return {'msg':'nao salvo'}