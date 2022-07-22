
import os, time
import classes

def init_game():
	# init electric type
	electric_type = classes.Type('Electric')

	# init move 1
	pikachu_move_1 = classes.Move('Thunder Shock', 40, 100, 30, electric_type, classes.Move.SPECIAL)

	# init pokemon 1
	pikachu = classes.Pokemon(
			name='Pikachu',
			hp=100,
			types=['electric',],
			moves=[pikachu_move_1.category,]
		)
