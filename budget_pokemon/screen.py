
import os, time


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