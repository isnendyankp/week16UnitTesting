from flask import Blueprint
from app import app

# Create a blueprint object
pokemon_blueprint = Blueprint('pokemon_endpoint', __name__)

@app.route('/', methods=['GET'])
def get_pokemon():
    return 'Get Pokemon'
