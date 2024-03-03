from . import main
from flask import render_template, request, flash, url_for,  redirect, jsonify
import requests
from .forms import PokemonForm, BattleForm
from  app.models import Pokemon, db, User, My_Pokemon 

from flask_login import current_user, login_required


@main.route("/")
def home():
    return render_template('home.html')

@main.route('/user/<name>')
def user(name):
    return f'hello {name}'





def get_pokemon_data(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    output=[]
    if response.ok:
        data = response.json()
        return {
            'name': data['name'].capitalize(),
            'hp': data['stats'][0]['base_stat'],
            'defense': data['stats'][3]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'sprite': data['sprites']['front_shiny'],
            'ability': data['abilities'][0]['ability']['name']
        }
    else:
        return output.append
pokemon_names = ['charizard', 'pikachu', 'squirtle', 'bulbasaur', 'charmander', 'raichu']

@main.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = PokemonForm()
    if request.method == 'POST' and form.validate_on_submit:
        pokemon_identifier = form.name_or_id.data
        print(pokemon_identifier)
        pokemons = get_pokemon_data(pokemon_identifier)
        return render_template('pokemon.html', pokemons=pokemons, form=form)
    else:
        return render_template('pokemon.html', form=form)
    
@main.route('/battleForm', methods=['POST'])
def battle():
    # Assuming you're receiving the usernames of the two users battling
    user1_name = request.form.get('user1')
    user2_name = request.form.get('user2')

    user1 = User.query.filter_by(username=user1_name).first()
    user2 = User.query.filter_by(username=user2_name).first()

    if not user1 or not user2:
        return jsonify({'error': 'One or both users not found'}), 404

    # Calculate the total stats for each team
    team1_stats = sum([p.base_attack + p.base_defense + p.base_hp for p in user1.pokemons])
    team2_stats = sum([p.base_attack + p.base_defense + p.base_hp for p in user2.pokemons])

    # Determine winner based on total stats
    if team1_stats > team2_stats:
        winner = user1.username
    elif team2_stats > team1_stats:
        winner = user2.username
    else:
        winner = "It's a tie!"

    return jsonify({'winner': winner}) 