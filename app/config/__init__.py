from flask import Flask


from app.config import database_config,migrate_config

def init_app(app:Flask):
    app.config['JSON_SORT_KEYS'] = False
    database_config.init_app(app)
    migrate_config.init_app(app)
