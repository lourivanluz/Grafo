from flask import Blueprint


from app.controller import distance_controller

bp_distance = Blueprint('distance',__name__,url_prefix='/distance')

bp_distance.post('/<graphId>/from/<town1>/to/<town2>')(distance_controller.search_shortest_distance)