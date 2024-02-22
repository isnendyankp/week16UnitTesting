from flask import Blueprint


# Create a blueprint object
pokemon_blueprint = Blueprint('pokemon_endpoint', __name__)

@pokemon_blueprint.route("/", methods=["GET"])
def get_pokemon():
    return 'Get Pokemon'
