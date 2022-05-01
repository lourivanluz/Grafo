from flask import current_app
from sqlalchemy.orm.session import Session


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
        

    def search_deep_all_path(self,start,finish):
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
                    path_list.append(current_paths+noh)
                    stack.append(noh)
 
        return finish_paths

    def calculate_route(self,routes):
        path_calculated = {}
        for path in routes:
            value = 0
            for index,noh in enumerate(path[1:]):
                index_start = self.noh.index(path[index])
                index_finish = self.noh.index(noh)
                value+=self.graph[index_start][index_finish]
            path_calculated[path]=value
        return path_calculated
        
    def save_in_db(self):
        session:Session = current_app.db.session
        qnt_noh = len(self.noh)
        qnt_connections = len(self.data)
        new_graph = Graph(qnt_noh=qnt_noh,qnt_connections=qnt_connections)
        session.add(new_graph)
        for connection in self.data:
            new_path = Path(**connection)
            new_graph_path = Graph_Path()
            new_graph_path.graphRef = new_graph
            new_graph_path.pathRef = new_path
            session.add(new_path)
            session.add(new_graph_path)
        session.commit()
        return new_graph