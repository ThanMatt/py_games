
import os, time
import classes
import json

script_dir = os.path.dirname(__file__)

pokemon_data = {}
types_data = {}

types = []
pokemons = []

def init_json(path):
	# :: Initializes json files

	file_path = os.path.join(script_dir, path)
	file = open(file_path, 'r')
	data = json.load(file)
	return data

def init_moves(moves):
	# :: Creates class for each Pokemon move
	moves_arr = []
	for move in moves:
		move_obj = classes.Move(
			name=move["name"],
			damage=move["damage"],
			pp=move["pp"],
			move_type=move["move_type"],
			accuracy=move["accuracy"],
			status_ailment=move["status_ailment"]
		)
		move_obj.category=move_obj.map_status(move["category"])
		moves_arr.append(move_obj)

	return moves_arr

def init_types_for_pokemon(types, const_types):
	# :: Maps the initialized Types array to the Pokemon types

	types_arr = []
	for typ in types:
		for i in const_types:
			if(i.map_name(typ)):
				types_arr.append(i)

def init_game():
	# :: Initialize global variables
	global pokemon_data, types_data
	global types, pokemon

	# :: Initialize json files
	pokemon_data = init_json('json/monsters.json')
	types_data = init_json('json/types.json')

	# :: Initialize main Types classes
	for type_data in types_data['types']:
		name = type_data+'_obj'
		name = classes.Type(
			name=type_data
		)
		print(name)
		types.append(name)


	# :: Initialize pokemons
	for pokemon in pokemon_data['pokemons']:
		pokemon_obj = classes.Pokemon(
			name=pokemon["name"],
			hp=pokemon["hp"],
			weaknesses=pokemon["weaknesses"],
			strengths=pokemon["strengths"],
			speed=pokemon["speed"]
		)
		pokemon_obj.set_types(init_types_for_pokemon(pokemon["types"], types))
		pokemon_obj.set_moves(init_moves(pokemon["moves"]))
		pokemons.append(pokemon_obj)
		

	for pokemon in pokemons:
		print(pokemon.get_name(), pokemon.get_speed())
		print(pokemon.types)
		# for move in pokemon.moves:
		# 	print(move.category)


