from flask import Flask
from app.route import pokemon_route

app = Flask(__name__)

# register the blueprints
app.register_blueprint(pokemon_route.pokemon_blueprint, url_prefix="/pokemons")