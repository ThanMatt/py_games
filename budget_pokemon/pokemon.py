import os, time

opponent_tab= "\t\t\t\t\t\t\t\t\t\t\t"
player_tab = "\t"

def print_bulbasaur_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "                                           /")
	print(tab, "                        _,.------....___,.' ',.-.")
	print(tab, "                     ,-'          _,.--\"        |")
	print(tab, "                   ,'         _.-'              .")
	print(tab, "                  /   ,     ,'                   `")
	print(tab, "                 .   /     /                     ``.")
	print(tab, "                 |  |     .                       \\.\\")
	print(tab, "       ____      |___._.  |       __               \\ `.")
	print(tab, "     .'    `---\"\"       ``\"-.--\"'`  \\               .  \\")
	print(tab, "    .  ,            __               `              |   .")
	print(tab, "    `,'         ,-\"'  .               \\             |    L")
	print(tab, "   ,'          '    _.'                -._          /    |")
	print(tab, "  ,`-.    ,\".   `--'                      >.      ,'     |")
	print(tab, " . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'")
	print(tab, " ||:, .           ,'  ;  /  / \\ `        `.    .      .'/")
	print(tab, " j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /")
	print(tab, "/ L:_  |                 .  \"' :_;                `.'.'")
	print(tab, ".    \"\"'                  \"\"\"\"\"'                    V")
	print(tab, " `.                                 .    `.   _,..  `")
	print(tab, "   `,_   .    .                _,-'/    .. `,'   __  `")
	print(tab, "    ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .")
	print(tab, "   /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |")
	print(tab, "  .   _  `\"\"'--.._____..--\"   ,             '         |")
	print(tab, "  | .\" `. `-.                /-.           /          ,")
	print(tab, "  | `._.'    `,_            ;  /         ,'          .")
	print(tab, " .'          /| `-.        . ,'         ,           ,")
	print(tab, " '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'")
	print(tab, " `\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' mh")

def print_charmander_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "              _.--\"\"`-..")
	print(tab, "            ,'          `.")
	print(tab, "          ,'          __  `.")
	print(tab, "         /|          \" __   \\")
	print(tab, "        , |           / |.   .")
	print(tab, "        |,'          !_.'|   |")
	print(tab, "      ,'             '   |   |")
	print(tab, "     /              |`--'|   |")
	print(tab, "    |                `---'   |")
	print(tab, "     .   ,                   |                       ,\".")
	print(tab, "      ._     '           _'  |                    , ' \\ `")
	print(tab, "  `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|")
	print(tab, "  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\")
	print(tab, "-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .")
	print(tab, "  `,         \"\"\"\"'     `.              ,'         |   |  ',,")
	print(tab, "    `.      '            '            /          '    |'. |/")
	print(tab, "      `.   |              \\       _,-'           |       ''")
	print(tab, "        `._'               \\   '\"\\                .      |")
	print(tab, "           |                '     \\                `._  ,'")
	print(tab, "           |                 '     \\                 .'|")
	print(tab, "           |                 .      \\                | |")
	print(tab, "           |                 |       L              ,' |")
	print(tab, "           `                 |       |             /   '")
	print(tab, "            \\                |       |           ,'   /")
	print(tab, "          ,' \\               |  _.._ ,-..___,..-'    ,'")
	print(tab, "         /     .             .      `!             ,j'")
	print(tab, "        /       `.          /        .           .'/")
	print(tab, "       .          `.       /         |        _.'.'")
	print(tab, "        `.          7`'---'          |------\"'_.'")
	print(tab, "       _,.`,_     _'                ,''-----\"'")
	print(tab, "   _,-_    '       `.     .'      ,\\")
	print(tab, "   -\" /`.         _,'     | _  _  _.|")
	print(tab, "    \"\"--'---\"\"\"\"\"'        `' '! |! /")
	print(tab, "                            `\" \" -' mh")

def print_squirtle_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "               _,........__")
	print(tab, "            ,-'            \"`-.")
	print(tab, "          ,'                   `-.")
	print(tab, "        ,'                        \\")
	print(tab, "      ,'                           .")
	print(tab, "      .'\\               ,\"\".       `")
	print(tab, "     ._.'|             / |  `       \\")
	print(tab, "     |   |            `-.'  ||       `.")
	print(tab, "     |   |            '-._,'||       | \\")
	print(tab, "     .`.,'             `..,'.'       , |`-.")
	print(tab, "     l                       .'`.  _/  |   `.")
	print(tab, "     `-.._'-   ,          _ _'   -\" \\  .     `")
	print(tab, "`.\"\"\"\"\"'-.`-...,---------','         `. `....__.")
	print(tab, ".'        `\"-..___      __,'\\          \\  \\     \\")
	print(tab, "\\_ .          |   `\"\"\"\"'    `.           . \\     \\")
	print(tab, "  `.          |              `.          |  .     L")
	print(tab, "    `.        |`--...________.'.        j   |     |")
	print(tab, "      `._    .'      |          `.     .|   ,     |")
	print(tab, "         `--,\\       .            `7\"\"' |  ,      |")
	print(tab, "            ` `      `            /     |  |      |    _,-'\"\"\"`-.")
	print(tab, "             \\ `.     .          /      |  '      |  ,'          `.")
	print(tab, "              \\  v.__  .        '       .   \\    /| /              \\")
	print(tab, "               \\/    `\"\"\\\"\"\"\"\"\"\"`.       \\   \\  /.''                |")
	print(tab, "                `        .        `._ ___,j.  `/ .-       ,---.     |")
	print(tab, "                ,`-.      \\         .\"     `.  |/        j     `    |")
	print(tab, "               /    `.     \\       /         \\ /         |     /    j")
	print(tab, "              |       `-.   7-.._ .          |\"          '         /")
	print(tab, "              |          `./_    `|          |            .     _,'")
	print(tab, "              `.           / `----|          |-............`---'")
	print(tab, "                \\          \\      |          |")
	print(tab, "               ,'           )     `.         |")
	print(tab, "                7____,,..--'      /          |")
	print(tab, "                                  `---.__,--.'mh")

def print_pidgey_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "                   .,")
	print(tab, "            , _.-','")
	print(tab, "          \"\"|\"    `\"\"\"\".,")
	print(tab, "         /'/       __.-'-\"/")
	print(tab, "        ','  _,--\"\"      '-._")
	print(tab, "    _...`...'.\"\"\"\"\"\".\\\"\"-----'")
	print(tab, " ,-'          `-.) /  `.  \\")
	print(tab, "+---.\"-.    |     `.    .  \\")
	print(tab, "     \\  `.  |       \\   |   L")
	print(tab, "      `v  ,-j        , .'   |")
	print(tab, "     .'\\,' /        /,'      -._")
	print(tab, "    ,____.'        .            `-.")
	print(tab, "        |         /                `-.")
	print(tab, "       /          `.                  `-.")
	print(tab, "      /             `. |                 `.                  _.")
	print(tab, "     .                `|                 ,-.             _.-\" .")
	print(tab, "    j                  |                 |  \\         _.'    /")
	print(tab, "    .                  |               .'    \\     ,-'      /")
	print(tab, "    |                  |            ,-.\\      \\  ,'      _.-")
	print(tab, "    |                . '  `.       |   `      `v'  _,.-\"/")
	print(tab, "    ||    \\          |  ` |(`'-`.,.j         \\ `.-'----+---.")
	print(tab, "    |'|   |L    \\  | |   `|   \\'              L \\___      /")
	print(tab, "    ' L   |`     L | |     `.                 | j   `\"\"\"-'")
	print(tab, "       `-'||\\    | ||j       `.       ._    ` '.")
	print(tab, "          `\\ '\"`^\"- '          `.       \\    |/|")
	print(tab, "            `._                  `-.     \\   Y |")
	print(tab, "    __,..-\"\"`..`._                  `-._  `\\ `.|")
	print(tab, "   +.....>+----.' \"\"----.........,--\"\"\" `--.'.'")
	print(tab, "       ,' _\\  ,..--.-\"' __>---'  |")
	print(tab, "      --\"\"  \"'  _.\" }<\"\"          `---\"\"`._")
	print(tab, "               /...\"  L__.+--   _,......'..'")
	print(tab, "                 /.-\"\"'/   \\ ,-'")
	print(tab, "                     .' ,-\"\"'")
	print(tab, "                    /.-' mh")

def print_pikachu_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "                                             ,-.")
	print(tab, "                                          _.|  '")
	print(tab, "                                        .'  | /")
	print(tab, "                                      ,'    |'")
	print(tab, "                                     /      /")
	print(tab, "                       _..----\"\"---.'      /")
	print(tab, " _.....---------...,-\"\"                  ,'")
	print(tab, " `-._  \\                                /")
	print(tab, "     `-.+_            __           ,--. .")
	print(tab, "          `-.._     .:  ).        (`--\"| \\")
	print(tab, "               7    | `\" |         `...'  \\")
	print(tab, "               |     `--'     '+\"        ,\". ,\"\"-")
	print(tab, "               |   _...        .____     | |/    '")
	print(tab, "          _.   |  .    `.  '--\"   /      `./     j")
	print(tab, "         \\' `-.|  '     |   `.   /        /     /")
	print(tab, "         '     `-. `---\"      `-\"        /     /")
	print(tab, "          \\       `.                  _,'     /")
	print(tab, "           \\        `                        .")
	print(tab, "            \\                                j")
	print(tab, "             \\                              /")
	print(tab, "              `.                           .")
	print(tab, "                +                          \\")
	print(tab, "                |                           L")
	print(tab, "                |                           |")
	print(tab, "                |  _ /,                     |")
	print(tab, "                | | L)'..                   |")
	print(tab, "                | .    | `                  |")
	print(tab, "                '  \\'   L                   '")
	print(tab, "                 \\  \\   |                  j")
	print(tab, "                  `. `__'                 /")
	print(tab, "                _,.--.---........__      /")
	print(tab, "               ---.,'---`         |   -j\"")
	print(tab, "                .-'  '....__      L    |")
	print(tab, "              \"\"--..    _,-'       \\ l||")
	print(tab, "                  ,-'  .....------. `||'")
	print(tab, "               _,'                /")
	print(tab, "             ,'                  /")
	print(tab, "            '---------+-        /")
	print(tab, "                     /         /")
	print(tab, "                   .'         /")
	print(tab, "                 .'          /")
	print(tab, "               ,'           /")
	print(tab, "             _'....----\"\"\"\"\" mh")

def print_sandshrew_opponent():
	global opponent_tab
	tab = opponent_tab
	print(tab, "          _...-----'`._")
	print(tab, "      _,-'   _`. .\"\". \\`._")
	print(tab, "    ,'    ,-'   ` ` |  \\/--.")
	print(tab, "  ,:_  ,-'       ` `|  |`.  `.")
	print(tab, " /   `'-..        `  .-'  `   \\")
	print(tab, "j         `.--,    \\       `   :")
	print(tab, "|         '--' |    \\       `._'-.")
	print(tab, "|___     |     |     L      .'    `.")
	print(tab, "|   `-. /|___.' `.   |    .'.       .")
	print(tab, "|     ,'          .  j.  /   `.      \\")
	print(tab, ".  _,'            |,'  `.      \\   ,<`.")
	print(tab, " .'             _.-      `      j.'  \\ \\                          ,.")
	print(tab, "  `       ,v-\"\"'   \\      )__,+'      . \\                       ,' |")
	print(tab, "   `.    / |  /  _,'`.  ,'  \\  \\       /`.                   _.:   |")
	print(tab, "     `,-'-`  / ,'     \\'    j,  \\   ,.'   L               ,-'   . F")
	print(tab, "     / ,. | / .        \\  .'     \\.-\\     |         _,.-\"`.     `,'")
	print(tab, "     (_\\/|'|   \\        .'   _,-\"    `    +....---+'       `     '")
	print(tab, "     . \\ |.     \\    ,.^---`<_        | ,'||       \\        \\   /")
	print(tab, "      `.'| \\_    :v-'         `.      |-  | \\ __..--\\     _,'\\,'")
	print(tab, "        `'/`----'/              '.  ,'    |  Y       L_,-'  ,'")
	print(tab, "          \\     /            ___,.'\\     j   |       |    .'")
	print(tab, "           \\   .\"`\",\"\"'\"\"\"'\"`     | .   .'   |       |  ,'")
	print(tab, "            \\  |   |         |    | | .' j,.-|       j-'")
	print(tab, "             `. ___|________/.....|_Y'  /    |   _.-'")
	print(tab, "          __,-' \\                 |    /    _j,-'")
	print(tab, "         '--.    .                `...+---\"\"")
	print(tab, "        `_____\\  _`..__    __,..-\"'")
	print(tab, "              .-'_|._  `\"\"\"       \\")
	print(tab, "             , -'    .          __/")
	print(tab, "             \"------------\"\"\"\"\"\" mh")

def print_charmander():
	global player_tab
	tab = player_tab
	print(tab, "              _.--\"\"`-..")
	print(tab, "            ,'          `.")
	print(tab, "          ,'          __  `.")
	print(tab, "         /|          \" __   \\")
	print(tab, "        , |           / |.   .")
	print(tab, "        |,'          !_.'|   |")
	print(tab, "      ,'             '   |   |")
	print(tab, "     /              |`--'|   |")
	print(tab, "    |                `---'   |")
	print(tab, "     .   ,                   |                       ,\".")
	print(tab, "      ._     '           _'  |                    , ' \\ `")
	print(tab, "  `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|")
	print(tab, "  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\")
	print(tab, "-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .")
	print(tab, "  `,         \"\"\"\"'     `.              ,'         |   |  ',,")
	print(tab, "    `.      '            '            /          '    |'. |/")
	print(tab, "      `.   |              \\       _,-'           |       ''")
	print(tab, "        `._'               \\   '\"\\                .      |")
	print(tab, "           |                '     \\                `._  ,'")
	print(tab, "           |                 '     \\                 .'|")

def print_bulbasaur():
	global player_tab
	tab = player_tab
	print(tab, "                                           /")
	print(tab, "                        _,.------....___,.' ',.-.")
	print(tab, "                     ,-'          _,.--\"        |")
	print(tab, "                   ,'         _.-'              .")
	print(tab, "                  /   ,     ,'                   `")
	print(tab, "                 .   /     /                     ``.")
	print(tab, "                 |  |     .                       \\.\\")
	print(tab, "       ____      |___._.  |       __               \\ `.")
	print(tab, "     .'    `---\"\"       ``\"-.--\"'`  \\               .  \\")
	print(tab, "    .  ,            __               `              |   .")
	print(tab, "    `,'         ,-\"'  .               \\             |    L")
	print(tab, "   ,'          '    _.'                -._          /    |")
	print(tab, "  ,`-.    ,\".   `--'                      >.      ,'     |")
	print(tab, " . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'")
	print(tab, " ||:, .           ,'  ;  /  / \\ `        `.    .      .'/")
	print(tab, " j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /")
	print(tab, "/ L:_  |                 .  \"' :_;                `.'.'")
	print(tab, ".    \"\"'                  \"\"\"\"\"'                    V")

def print_squirtle():
	global player_tab
	tab = player_tab
	print(tab, "               _,........__")
	print(tab, "            ,-'            \"`-.")
	print(tab, "          ,'                   `-.")
	print(tab, "        ,'                        \\")
	print(tab, "      ,'                           .")
	print(tab, "      .'\\               ,\"\".       `")
	print(tab, "     ._.'|             / |  `       \\")
	print(tab, "     |   |            `-.'  ||       `.")
	print(tab, "     |   |            '-._,'||       | \\")
	print(tab, "     .`.,'             `..,'.'       , |`-.")
	print(tab, "     l                       .'`.  _/  |   `.")
	print(tab, "     `-.._'-   ,          _ _'   -\" \\  .     `")
	print(tab, "`.\"\"\"\"\"'-.`-...,---------','         `. `....__.")
	print(tab, ".'        `\"-..___      __,'\\          \\  \\     \\")
	print(tab, "\\_ .          |   `\"\"\"\"'    `.           . \\     \\")
	print(tab, "  `.          |              `.          |  .     L")

def print_pidgey():
	global player_tab
	tab = player_tab
	print(tab, "                   .,")
	print(tab, "            , _.-','")
	print(tab, "          \"\"|\"    `\"\"\"\".,")
	print(tab, "         /'/       __.-'-\"/")
	print(tab, "        ','  _,--\"\"      '-._")
	print(tab, "    _...`...'.\"\"\"\"\"\".\\\"\"-----'")
	print(tab, " ,-'          `-.) /  `.  \\")
	print(tab, "+---.\"-.    |     `.    .  \\")
	print(tab, "     \\  `.  |       \\   |   L")
	print(tab, "      `v  ,-j        , .'   |")
	print(tab, "     .'\\,' /        /,'      -._")
	print(tab, "    ,____.'        .            `-.")
	print(tab, "        |         /                `-.")
	print(tab, "       /          `.                  `-.")

def print_pikachu():
	global player_tab
	tab = player_tab
	print(tab, "                                             ,-.")
	print(tab, "                                          _.|  '")
	print(tab, "                                        .'  | /")
	print(tab, "                                      ,'    |'")
	print(tab, "                                     /      /")
	print(tab, "                       _..----\"\"---.'      /")
	print(tab, " _.....---------...,-\"\"                  ,'")
	print(tab, " `-._  \\                                /")
	print(tab, "     `-.+_            __           ,--. .")
	print(tab, "          `-.._     .:  ).        (`--\"| \\")
	print(tab, "               7    | `\" |         `...'  \\")
	print(tab, "               |     `--'     '+\"        ,\". ,\"\"-")
	print(tab, "               |   _...        .____     | |/    '")
	print(tab, "          _.   |  .    `.  '--\"   /      `./     j")
	print(tab, "         \\' `-.|  '     |   `.   /        /     /")
	print(tab, "         '     `-. `---\"      `-\"        /     /")
	print(tab, "          \\       `.                  _,'     /")
	print(tab, "           \\        `                        .")

def print_sandshrew():
	global player_tab
	tab = player_tab
	print(tab, "          _...-----'`._")
	print(tab, "      _,-'   _`. .\"\". \\`._")
	print(tab, "    ,'    ,-'   ` ` |  \\/--.")
	print(tab, "  ,:_  ,-'       ` `|  |`.  `.")
	print(tab, " /   `'-..        `  .-'  `   \\")
	print(tab, "j         `.--,    \\       `   :")
	print(tab, "|         '--' |    \\       `._'-.")
	print(tab, "|___     |     |     L      .'    `.")
	print(tab, "|   `-. /|___.' `.   |    .'.       .")
	print(tab, "|     ,'          .  j.  /   `.      \\")
	print(tab, ".  _,'            |,'  `.      \\   ,<`.")
	print(tab, " .'             _.-      `      j.'  \\ \\                          ,.")
	print(tab, "  `       ,v-\"\"'   \\      )__,+'      . \\                       ,' |")
	print(tab, "   `.    / |  /  _,'`.  ,'  \\  \\       /`.                   _.:   |")
	print(tab, "     `,-'-`  / ,'     \\'    j,  \\   ,.'   L               ,-'   . F")
	print(tab, "     / ,. | / .        \\  .'     \\.-\\     |         _,.-\"`.     `,'")

def print_pokemon(name):
	switch = {
		'Sandshrew': print_sandshrew,
		'Pikachu': print_pikachu,
		'Squirtle': print_squirtle,
		'Charmander': print_charmander,
		'Pidgey': print_pidgey,
		'Bulbasaur': print_bulbasaur
	}
	print_function = switch.get(name)
	print_function()

def print_pokemon_opponent(name):
	switch = {
		'Sandshrew': print_sandshrew_opponent,
		'Pikachu': print_pikachu_opponent,
		'Squirtle': print_squirtle_opponent,
		'Charmander': print_charmander_opponent,
		'Pidgey': print_pidgey_opponent,
		'Bulbasaur': print_bulbasaur_opponent
	}
	print_function = switch.get(name)
	print_function()

def animate_attack(print_pokemon, tab):
	newline = "\n"
	for i in range(0, 4):
		if i%2==0:
			for j in range(0, 4):
				os.system("clear")
				print(newline*j)
				print_pokemon(tab)
				time.sleep(0.001)
		else:
			for j in range(4, 0, -1):
				os.system("clear")
				print(newline*j)
				print_pokemon(tab)
				time.sleep(0.001)
		time.sleep(0.1)

def animate_miss(print_pokemon, tab):
	newline = "\n"
	for i in range(0, 4):
		if i%2==0:
			for j in range(0, 4):
				os.system("clear")
				print_pokemon(tab*j)
				time.sleep(0.001)
		else:
			for j in range(4, 0, -1):
				os.system("clear")
				print_pokemon(tab*j)
				time.sleep(0.001)
		time.sleep(0.1)
