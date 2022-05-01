from dataclasses import dataclass
from sqlalchemy import Column,Integer,String


from app.config.database_config import db
from app.services.entiti_services import create_uuid

@dataclass
class Path(db.Model):
    path_id:str
    source:str
    target:str
    distance:int

    __tablename__= 'path'

    path_id              = Column(String,primary_key=True,default=create_uuid)
    source               = Column(String,nullable=False)
    target               = Column(String,nullable=False)
    distance             = Column(Integer,nullable=False)