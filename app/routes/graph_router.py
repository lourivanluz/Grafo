from flask import Blueprint

from app.controller import graph_controller

bp_graph = Blueprint('graph',__name__,url_prefix='/graph')

bp_graph.post('')(graph_controller.create_graph)
bp_graph.get('/<graphId>')(graph_controller.retriver_graph)
