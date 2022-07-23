
import os, time
import classes
import json

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'json/monsters.json')
monsters = open(file_path, 'r')
data = json.load(monsters)


def init_game():
	# init electric type
	electric_type = classes.Type('Electric')

	# :: Pokemons to choose
	pokemons = []

	# init move 1
	pikachu_move_1 = classes.Move('Thunder Shock', 40, 100, 30, electric_type, classes.Move.SPECIAL)

	# :: Initialize pokemons
	for pokemon in data['pokemons']:
		pokemons.append(
			classes.Pokemon(
				name=pokemon["name"],
				hp=pokemon["hp"],
				types=pokemon["types"],
				weaknesses=pokemon["weaknesses"],
				strengths=pokemon["strengths"],
				moves=pokemon["moves"],
				speed=pokemon["speed"]
			)
		)

	for pokemon in pokemons:
		print(pokemon.get_name(), pokemon.get_speed())
	# init pokemon 1
	# pikachu = classes.Pokemon(
	# 		name='Pikachu',
	# 		hp=100,
	# 		types=['electric',],
	# 		moves=[pikachu_move_1.category,]
	# 	)

init_game()