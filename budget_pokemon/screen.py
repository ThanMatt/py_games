
import os, time, math

#di daw gagamitin sabi ni baho >:(
# def battle_screen():
# 	width = 140
# 	os.system("clear")
# 	print("\x1b[8;170;170t")
# 	space = " "
# 	overscore = "⎻"
# 	underscore = "_"
# 	broken_line = "- "
# 	double_pipe = "\t||"
# 	pipe = "|"
# 	print("\t", underscore*153)
# 	print("\t", broken_line*77)
# 	for i in range(0, 40):
# 		if(i==3):
# 			print(double_pipe, space*8, pipe, overscore*40, pipe, space*(width-(40+8)), double_pipe)
# 		elif(i>3 and i<=9):
# 			print(double_pipe, space*8, pipe, space*40, pipe, space*(width-(40+8)), double_pipe)
# 		elif(i==10):
# 			print(double_pipe, space*8, pipe, underscore*40, pipe, space*(width-(40+8)), double_pipe)
# 		elif(i==25):
# 			print(double_pipe, space*87, pipe, overscore*40, pipe, space*(width-(40+87)), double_pipe)
# 		elif(i>25 and i<=31):
# 			print(double_pipe, space*87, pipe, space*40, pipe, space*(width-(40+87)), double_pipe)
# 		elif(i==32):
# 			print(double_pipe, space*87, pipe, underscore*40, pipe, space*(width-(40+87)), double_pipe)
# 		else:
# 			print(double_pipe, space*width, double_pipe)
# 	print("\t", broken_line*77)
# 	print("\t", overscore*153)

tab = "\t"
space = " "
overscore = "⎻"
underscore = "_"
broken_line = "- "
double_pipe = "\t||"
pipe = "|"

# move1 = "Water Gun"
# move2 = "Bubble Beam"
# move3 = "Pound"
# move4 = "Hydro Pump"

# string3 = "<name> is <inflicted_status> <name> used <move>"
# string = "What will <name> do?"
# string2 = "<name> is paralyzed, it can't move"


def compute_space_needed(width, word):
	space_needed = width - len(word)
	return space_needed

def compute_half(width, word):
	space_needed = compute_space_needed(width, word)
	half = math.ceil(space_needed/2)
	return half

def compute_difference(width, word):
	# print(compute_space_needed(width, word) - compute_half(width, word))
	return compute_space_needed(width, word) - compute_half(width, word)

def battle_screen(message, player):
	print("\x1b[8;170;170t")
	menu(message, player.moves[0].name, player.moves[1].name, 
	player.moves[2].name, player.moves[3].name)
	print()

def build_move_row(move1, move2, menu_width):
	print(
		tab*2, space*2, pipe, space*menu_width, pipe, pipe, 

		space*compute_difference(math.floor(menu_width/2), move1), move1, 
		space*(compute_half(math.ceil(menu_width/2), move1)-2), pipe,

		space*compute_difference(math.floor(menu_width/3), move2), move2, 
		space*(compute_half(math.ceil(menu_width/2), move2)), pipe
	)

def build_space_around(menu_width):
	print(
		tab*2, space*2, pipe, space*menu_width, pipe, 
		pipe, space*math.ceil(menu_width/2), pipe, 
		space*(math.floor(menu_width/2)-3), pipe
	)

def build_borders(symbol, menu_width):
	print(tab*2, space*2, pipe, symbol*menu_width, pipe, pipe, symbol*menu_width, pipe)


def menu(message, move1, move2, move3, move4):
	menu_width = 60

	space_needed = menu_width - len(message)
	half = math.ceil(space_needed/2)

	build_borders(overscore, menu_width)
	build_space_around(menu_width)
	build_move_row(move1, move2, menu_width)
	build_space_around(menu_width)

	print(tab*2, space*2, pipe, space*compute_difference(menu_width, message), message, 
		space*(compute_half(menu_width, message)-2), pipe, pipe, underscore*menu_width, pipe,)

	build_space_around(menu_width)
	build_move_row(move3, move4, menu_width)
	build_space_around(menu_width)
	build_borders(underscore, menu_width)


def choose():
	newline = "\n\n"
	for i in range(0, 11):
		os.system("clear")
		print(newline*i)
		print("\t\t\t\t\t    █▀▀ █░█ █▀█ █▀█ █▀ █▀▀   █▄█ █▀█ █░█ █▀█   █▀█ █▀█ █▄▀ █▀▀ █▀▄▀█ █▀█ █▄░█ ")
		print("\t\t\t\t\t    █▄▄ █▀█ █▄█ █▄█ ▄█ ██▄   ░█░ █▄█ █▄█ █▀▄   █▀▀ █▄█ █░█ ██▄ █░▀░█ █▄█ █░▀█ ")
		time.sleep(.5)
	pikachu()


def pikachu():
	tab="\t"
	newline = "\n\n"
	for i in range(10, 2, -1):
		os.system("clear")
		print(newline*5)
		print(tab*i, "`;-.          ___, ")
		print(tab*i, "  `.`\_...._/`.-\"` ")
		print(tab*i, "    \        /      ,")
		print(tab*i, "    /()   () \    .' `-._")
		print(tab*i, "   |)  .    ()\  /   _.' ")
		print(tab*i, "   \  -'-     ,; '. < ")
		print(tab*i, "    ;.__     ,;|   > \ ")
		print(tab*i, "   / ,    / ,  |.-'.-' ")
		print(tab*i, "  (_/    (_/ ,;|.<` ")
		print(tab*i, "    \    ,     ;-` ")
		print(tab*i, "     >   \    / ")
		print(tab*i, "    (_,-'`> .'")
		print(tab*i, "         (_,'")
		time.sleep(.5)



def start_screen():
	print("\x1b[8;170;170t")
	space=" "
	for j in range(0, 3):
		for i in range(0,3):
			print(i)
			print_start_screen()
			print("\t\t\t\t\t\t\t\t  █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀")
			print("\t\t\t\t\t\t\t\t  █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█", space*i, "▄")

			print("\n")
			print("\n")

			time.sleep(.5)


def print_start_screen():
	os.system("clear")

	print("\n")
	print("\n")
	print("\n")

	print("\t\t\t   ___               _            _ __  ")
	print("\t\t\t  / / |__  _   _  __| | __ _  ___| |\ \   ")
	print("\t\t\t | || '_ \| | | |/ _` |/ _` |/ _ \ __| |   ")
	print("\t\t\t | || |_) | |_| | (_| | (_| |  __/ |_| |    ")
	print("\t\t\t | ||_.__/ \__,_|\__,_|\__, |\___|\__| |    ")
	print("\t\t\t  \_\                  |___/        /_/     ")

	print("\n")
	print("\n")

	print("\t\t\t\t\t\t	                          ,'\                          ")
	print("\t\t\t\t\t\t    _.----.        ____         ,'  _\   ___    ___     ____    ")
	print("\t\t\t\t\t\t_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.  ")
	print("\t\t\t\t\t\t\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |  ")
	print("\t\t\t\t\t\t \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |    ")
	print("\t\t\t\t\t\t   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |   ")
	print("\t\t\t\t\t\t    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |    ")
	print("\t\t\t\t\t\t     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |   ")
	print("\t\t\t\t\t\t      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |   ")
	print("\t\t\t\t\t\t       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |    ")
	print("\t\t\t\t\t\t        \_.-'       |__|    `-._ |              '-.|     '-.| |   |    ")
	print("\t\t\t\t\t\t                                `'                            '-._|   ")

	print("\n")
	print("\n")
	print("\n")