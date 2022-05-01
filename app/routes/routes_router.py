from flask import Blueprint

from app.controller import routes_controller
bp_routes = Blueprint('routes',__name__,url_prefix='/routes')

bp_routes.post('/<graphId>/from/<town1>/to/<town2>')(routes_controller.search_router)