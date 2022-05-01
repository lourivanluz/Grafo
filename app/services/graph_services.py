from flask import current_app
from sqlalchemy import column
from sqlalchemy.orm import Query,Session


from app.models.classes.graph_class import Grafo
from app.models.entitis.graph_path_model import Graph_Path
from app.models.entitis.graph_model import Graph
from app.models.entitis.path_model import Path

def handle_data_graph(**data):
    noh_list = data.get('data')
    graph = Grafo(noh_list)
    if(graph.validate):
        session:Session = current_app.db.session
        saved_graph = graph.save_in_db()
        query:Query = (session.query(Path.source,Path.target,Path.distance)
        .select_from(Graph_Path)
        .join(Path)
        .filter(Graph_Path.graph_id == saved_graph.graph_id))

        column_names = [q['name'] for q in query.column_descriptions]
        serializer = [dict(zip(column_names,row)) for row in query.all()]


        return {'id':saved_graph.graph_id,'data':serializer}

    return {'msg':'nao salvo'}