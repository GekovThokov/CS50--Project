from flask import Blueprint 

views = Blueprint('views', __name__)

@views.routes('/')
def home():
    return "<h1>TEST</h1>"