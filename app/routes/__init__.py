from flask import Flask


from app.routes.graph_router import bp_graph
from app.routes.routes_router import bp_routes
from app.routes.distance_router import bp_distance
from app.routes.home_router import bp_home

def init_app(app:Flask):
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_graph)
    app.register_blueprint(bp_routes)
    app.register_blueprint(bp_distance)

    return app