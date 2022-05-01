from dataclasses import dataclass
from sqlalchemy import Column,Integer,String

from app.config.database_config import db
from app.services.entiti_services import create_uuid

@dataclass
class Graph(db.Model):
    graph_id:str
    qnt_connections:int
    qnt_noh:int

    __tablename__= 'graph'

    graph_id              = Column(String,primary_key=True,default=create_uuid)
    qnt_connections       = Column(Integer,nullable=False)
    qnt_noh               = Column(Integer,nullable=False)