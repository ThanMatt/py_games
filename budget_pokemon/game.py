# Pokemon Game

# sources:
	# pokemon text & art: https://www.asciiart.eu/video-games/pokemon
	# ascii text art: https://patorjk.com/software/taag/#p=display&f=Merlin1&t=loading%0A
	# ascii text art: https://fsymbols.com/generators/carty/
	# pokemon art: https://gist.github.com/MatheusFaria/4cbb8b6dbe33fd5605cf8b8f7130ba6d?fbclid=IwAR2-TQdesqqrLdX9v0NWTuPILPTD8fZBtykDD1kEilw1seF2pVwoJrGVFkk

import os, time
import screen, init, pokemon

action_message = ''
player1 = ''
player2 = ''

# screen.start_screen()
init.init_game()
# screen.choose()
# screen.battle_screen()


def print_roster(roster):
	for i in range(len(roster)):
		print("\t\t", i+1, ":", roster[i].name)

def init_pokemon_for_players():
	global player1, player2

	roster = init.pokemons
	print("\t\tPlayer 1, choose your pokemon: ")
	print_roster(roster)
	player1input = input("\t\t>> ")

	player1 = init.pokemons[int(player1input)-1]
	print("\t\t Player 1's pokemon:", player1.name)

	roster.remove(player1)

	print("\t\tPlayer 2, choose your pokemon: ")
	print_roster(roster)
	player2input = input("\t\t>> ")

	player2 = init.pokemons[int(player2input)-1]
	print("\t\t Player 2's pokemon:", player2.name)

	start_game()

def player1_screen(tabs_opponent, tabs_player):
	os.system("clear")
	# print_player1_function_name = 'print_' + player1.name.lower()
	# print_player2_function_name = 'print_' + player2.name.lower() + '_opponent'

	# print(print_player1_function_name)
	# # func = globals()[pokemon[print_player1_function_name]]
	# pokemon[func(tabs)]
	# screen.battle_screen()

def start_game():
	os.system("clear")
	tabs_opponent = "\t\t\t\t\t\t\t\t\t\t\t"
	tabs_player = "\t"
	player1_screen(tabs_opponent, tabs_player)
	# pokemon.print_bulbasaur_opponent(tabs_opponent)
	# pokemon.print_charmander(tabs_player)
	# screen.battle_screen()
	# print(init.pokemons)

init_pokemon_for_players()


# pokemon.animate_pokemon(pokemon.print_bulbasaur)
# pokemon.animate_pokemon(pokemon.print_pikachu)
# pokemon.animate_pokemon(pokemon.print_sandshrew)
# pokemon.animate_pokemon(pokemon.print_charmander)
# pokemon.animate_pokemon(pokemon.print_pidgey)
# pokemon.animate_pokemon(pokemon.print_squirtle)


