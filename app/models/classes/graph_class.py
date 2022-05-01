from flask import current_app
from sqlalchemy.orm import Session,Query


from app.models.entitis.graph_model import Graph
from app.models.entitis.path_model import Path
from app.models.entitis.graph_path_model import Graph_Path


class Grafo:
    def __init__(self,data):
        self.vertices,self.noh = self.generete_vertice_and_noh(data)
        self.graph,self.validate = self.generete_matriz_and_validate(data)
        self.connection,self.connectionFormated = self.generete_path()
        self.data = data



    def generete_matriz_and_validate(self,data):
        graph = []
        validate_graph=True
        for line in range(self.vertices):
            addline = []
            for column in range(self.vertices):
                addline.append(0)
            graph.append(addline)     
   
        for index,_ in enumerate(data):
            line = self.noh.index(data[index]["source"])
            column = self.noh.index(data[index]["target"])
            if(graph[line][column])!=0:
                graph = []
                validate_graph=False
                break
            graph[line][column] = data[index]['distance']
        return (graph,validate_graph) 
            
                
    def generete_path(self):
        connection = []
        connectionF = {}
        for index,line in enumerate(self.graph):
            addConection = []
            connectionF[self.noh[index]] = []
            for indexI,element in enumerate(line):
                if element!=0:
                    addConection.append(indexI)
                    connectionF[self.noh[index]].append(self.noh[indexI])
            connection.append(addConection)
        return (connection,connectionF)
    
    def generete_vertice_and_noh(self,data):
        points = []
        for vertice in data:
            if vertice["source"] not in points:
                points.append(vertice["source"])
            if vertice["target"] not in points:
                points.append(vertice["target"])
        return (len(points),points)
        

    def search_deep_all_path(self,start,finish,steps=0):
        connection = dict(self.connectionFormated)
        finish_paths = []
        current_paths = start
        path_list = [current_paths]
        stack = [] 
        stack.append(start)

        while len(stack)>0:
            current_noh = stack.pop()
            current_paths = path_list.pop()

            for noh in connection[current_noh]:
                if noh == finish:
                    finish_paths.append(current_paths+finish)

                elif noh not in current_paths:
                    new_path = current_paths+noh
                    if steps==0 or len(new_path)<=steps:
                        path_list.append(new_path)
                        stack.append(noh)
 
        return finish_paths

    def calculate_route(self,routes):
        result = []
        for path in routes:
            path_calculated={}
            value = 0
            for index,noh in enumerate(path[1:]):
                index_start = self.noh.index(path[index])
                index_finish = self.noh.index(noh)
                value+=self.graph[index_start][index_finish]
            path_calculated[path]=value
            result.append(path_calculated)
        return result
        
    def save_in_db(self):
        session:Session = current_app.db.session
        qnt_noh = len(self.noh)
        qnt_connections = len(self.data)
        new_graph = Graph(qnt_noh=qnt_noh,qnt_connections=qnt_connections)
        session.add(new_graph)
        for connection in self.data:

            old_path = Path.query.filter_by(**connection).first()  
  
            if old_path:
                new_path = old_path
            else :
                new_path = Path(**connection)
                session.add(new_path)

            new_graph_path = Graph_Path()
            new_graph_path.graphRef = new_graph
            new_graph_path.pathRef = new_path
            
            session.add(new_graph_path)
        session.commit()
        return new_graph
    
    @staticmethod
    def get_connections_by_graphid(graph_id):
        session:Session = current_app.db.session
        query:Query = (session.query(Path.source,Path.target,Path.distance)
        .select_from(Graph_Path)
        .join(Path)
        .filter(Graph_Path.graph_id == graph_id))

        column_names = [column['name'] for column in query.column_descriptions]
        serializer = [dict(zip(column_names,row)) for row in query.all()]
        return serializer