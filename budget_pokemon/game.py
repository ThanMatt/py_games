# Pokemon Game

# sources:
	# pokemon text & art: https://www.asciiart.eu/video-games/pokemon
	# ascii text art: https://patorjk.com/software/taag/#p=display&f=Merlin1&t=loading%0A
	# ascii text art: https://fsymbols.com/generators/carty/
	# pokemon art: https://gist.github.com/MatheusFaria/4cbb8b6dbe33fd5605cf8b8f7130ba6d?fbclid=IwAR2-TQdesqqrLdX9v0NWTuPILPTD8fZBtykDD1kEilw1seF2pVwoJrGVFkk

import os, time, random
import screen, init, pokemon

action_message = ''
player1 = ''
player2 = ''
double_tab = "\t\t"

p1_turn=True
p2_turn=False
missed=False

# screen.start_screen()
init.init_game()

def updateTurn(p1State, p2State):
	global p1_turn,p2_turn
	p1_turn=p1State
	p2_turn=p2State


def updateMissedTurn(missedTurn):
	global missed
	missed=missedTurn


def default_message(player):
	return 'What will ' + player.name + ' do?'


def set_message(string):
	global action_message
	action_message = string

def print_roster(roster):
	for i in range(len(roster)):
		print(double_tab, i+1, ":", roster[i].name)


def init_pokemon_for_players():
	global player1, player2

	roster = init.pokemons
	print(double_tab, "Player 1, choose your pokemon: ")
	print_roster(roster)
	player1input = input("\t\t>> ")

	player1 = init.pokemons[int(player1input)-1]
	print(double_tab, "Player 1's pokemon:", player1.name)

	roster.remove(player1)

	print(double_tab, "Player 2, choose your pokemon: ")
	print_roster(roster)
	player2input = input("\t\t>> ")

	player2 = init.pokemons[int(player2input)-1]
	print(double_tab, "Player 2's pokemon:", player2.name)

	start_game()


def game_status_checker():
	if player1.hp != 0 and player2.hp != 0:
		return True
	else:
		return False


def attack(attacker, move, receiver):
	chance = attacker.moves[move].accuracy
	if random.random() > chance:
		receiver.hp = receiver.hp - attacker.moves[move].damage
		pokemon.animate_attack(receiver.name)
	else:
		set_message(attacker.name + 'missed!')
		pokemon.animate_miss(receiver.name)


def player1_screen():
	os.system("clear")
	player2.print_pokemon_opponent()
	player1.print_pokemon_player()
	screen.battle_screen(action_message, player1)
	player_input = input("\t\t>> ")
	attack(player1, int(player_input), player2)


def player2_screen():
	os.system("clear")
	player1.print_pokemon_opponent()
	player2.print_pokemon_player()
	screen.battle_screen(action_message, player2)

def attack_sequence():
	# attack should be here determined by speed
	# if player1.speed > player2.speed (but should this be the case always?)
	# attack(player1, move, player2)
	# attack(player2, move, player1)

	# moves per round should be saved
	# move = player1.moves[int(player_input)]

	print()

def start_game():
	while(game_status_checker()):
		os.system("clear")
		if(p1_turn):
			set_message(default_message(player1))
			player1_screen()
		else:
			set_message(default_message(player2))
			player2_screen()

		# after showing player screen and getting user input for moves,
		# attack_sequence()
		
		if not missed:
			updateTurn(p2_turn, p1_turn)

		

init_pokemon_for_players()
