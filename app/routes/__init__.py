
from flask import Flask

from app.routes.graph_router import bp_graph
from app.routes.routes_router import bp_routes

def init_app(app:Flask):
    app.register_blueprint(bp_graph)
    app.register_blueprint(bp_routes)

    return app