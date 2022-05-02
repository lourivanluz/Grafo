from flask import Blueprint


from app.controller import home_controller

bp_home = Blueprint('home',__name__,url_prefix='/')

bp_home.get('')(home_controller.home)