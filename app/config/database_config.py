from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from app.models import entitis

db = SQLAlchemy()

def init_app(app:Flask):
 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.db = db
    entitis.import_entitis()