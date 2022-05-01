from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey,String
from sqlalchemy.orm import relationship,backref


from app.config.database_config import db
from app.models.entitis.graph_model import Graph
from app.models.entitis.path_model import Path
from app.services.entiti_services import create_uuid

@dataclass
class Graph_Path(db.Model):
    graph_path_id:int
    graph_id:Graph
    path_id:Path

    __tablename__ = 'graph_path'

    graph_path_id       = Column(String,primary_key=True,default=create_uuid)
    graph_id            = Column(String,ForeignKey('graph.graph_id'),nullable=True)
    path_id             = Column(String,ForeignKey('path.path_id'),nullable=True)

    graphRef = relationship('Graph',backref=backref('graph_path'))
    pathRef = relationship('Path',backref=backref('graph_path'))