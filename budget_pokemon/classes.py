
import pokemon

class Pokemon:
	def __init__(self, name, hp, speed):
		self.name = name
		self.hp = hp
		self.types = []
		self.moves = []
		self.speed = speed

	def get_name(self):
		return self.name
	
	def get_moves(self):
		return self.moves
	
	def get_speed(self):
		return self.speed

	def set_moves(self, moves):
		self.moves = moves

	def set_types(self, types):
		self.types = types
	
	def get_types(self):
		return self.types

	def print_pokemon_player(self):
		pokemon.print_pokemon(self.name, True)

	def print_pokemon_opponent(self):
		pokemon.print_pokemon_opponent(self.name, True)
	
	def get_print_pokemon_player(self):
		return pokemon.print_pokemon(self.name, False)
	
	def get_print_pokemon_opponent(self):
		return pokemon.print_pokemon_opponent(self.name, False)

class Move:
	PHYSICAL = 'Physical'
	SPECIAL = 'Special'
	STATUS = 'Status'

	def __init__(self, name, damage, accuracy, pp, status_ailment):
		self.name = name
		self.damage = damage
		self.accuracy = accuracy
		self.pp = pp
		self.move_type = []
		self.category = ''
		self.status_ailment = status_ailment

	def map_status(self, category):
		map_to_constant = {
			"Physical": self.PHYSICAL,
			"Special": self.SPECIAL,
			"Status": self.STATUS
		}
		return map_to_constant[category]

	def set_types(self, types):
		self.move_type = types


class Type:
	NORMAL="normal"
	FIRE="fire"
	WATER="water"
	GRASS="grass"
	ELECTRIC="electric"
	ICE="ice"
	FIGHTING="fighting"
	POISON="poison"
	GROUND="ground"
	FLYING="flying"
	PSYCHIC="psychic"
	BUG="bug"
	ROCK="rock"
	GHOST="ghost"
	DARK="dark"
	DRAGON="dragon"
	STEEL="steel"
	FAIRY="fairy"

	def __init__(self, name):
		self.name = name
		self.weakness = []
		self.strength = []

	def map_name(self, name):
		return self.name.lower() == name.lower()
	
	
	def get_name(self):
		return self.name
	

	def set_weakness(self, name, types):
		if name == self.NORMAL:
			weakness_types = [self.FIGHTING]
		elif name == self.FIRE:
			weakness_types = [self.WATER, self.GROUND, self.ROCK]
		elif name == self.WATER:
			weakness_types = [self.ELECTRIC, self.GRASS]
		elif name == self.GRASS:
			weakness_types = [self.FLYING, self.POISON, self.BUG, self.FIRE, self.ICE]
		elif name == self.ELECTRIC:
			weakness_types = [self.GROUND]
		elif name == self.PSYCHIC:
			weakness_types = [self.BUG, self.DARK, self.GHOST]
		elif name == self.ICE:
			weakness_types = [self.FIGHTING, self.ROCK, self.FIRE, self.STEEL]
		elif name == self.DRAGON:
			weakness_types = [self.DRAGON, self.ICE, self.FAIRY]
		elif name == self.DARK:
			weakness_types = [self.FIGHTING, self.BUG, self.FAIRY]
		elif name == self.FAIRY:
			weakness_types = [self.POISON, self.STEEL]
		elif name == self.FIGHTING:
			weakness_types = [self.FLYING, self.PSYCHIC, self.FAIRY]
		elif name == self.FLYING:
			weakness_types = [self.ROCK, self.ELECTRIC, self.ICE]
		elif name == self.POISON:
			weakness_types = [self.GROUND, self.PSYCHIC]
		elif name == self.GROUND:
			weakness_types = [self.WATER, self.GRASS, self.ICE]
		elif name == self.ROCK:
			weakness_types = [self.FIGHTING, self.GROUND, self.STEEL, self.WATER, self.GRASS]
		elif name == self.BUG:
			weakness_types = [self.FLYING, self.ROCK, self.FIRE]
		elif name == self.GHOST:
			weakness_types = [self.GHOST]
		elif name == self.STEEL:
			weakness_types = [self.FIGHTING, self.GROUND, self.FIRE]
		for weakness_type in weakness_types:
			self.weakness.append(self.__get_weakness_type(weakness_type, types))
			

	def set_strength(self, name, types):
		if name == self.NORMAL:
			strength_types = []
		elif name == self.FIRE:
			strength_types = [self.BUG, self.STEEL, self.FIRE, self.GRASS, self.ICE, self.FAIRY]
		elif name == self.WATER:
			strength_types = [self.WATER, self.FIRE, self.STEEL, self.ICE]
		elif name == self.GRASS:
			strength_types = [self.GRASS, self.WATER, self.GROUND, self.ELECTRIC]
		elif name == self.ELECTRIC:
			strength_types = [self.ELECTRIC, self.FLYING, self.STEEL]
		elif name == self.PSYCHIC:
			strength_types = [self.PSYCHIC, self.FIGHT]
		elif name == self.ICE:
			strength_types = [self.ICE]
		elif name == self.DRAGON:
			strength_types = [self.FIRE, self.WATER, self.GRASS, self.ELECTRIC]
		elif name == self.DARK:
			strength_types = [self.DARK, self.GHOST]
		elif name == self.FAIRY:
			strength_types = [self.FIGHTING, self.BUG, self.DARK]
		elif name == self.FIGHTING:
			strength_types = [self.ROCK, self.BUG, self.DARK]
		elif name == self.FLYING:
			strength_types = [self.FIGHTING, self.BUG, self.GRASS]
		elif name == self.POISON:
			strength_types = [self.POISON, self.FIGHTING, self.GRASS, self.FAIRY, self.BUG]
		elif name == self.GROUND:
			strength_types = [self.POISON, self.ROCK]
		elif name == self.ROCK:
			strength_types = [self.ROCK, self.NORMAL, self.FLYING, self.POISON, self.FIRE]
		elif name == self.BUG:
			strength_types = [self.FIGHTING, self.GROUND, self.GRASS]
		elif name == self.GHOST:
			strength_types = [self.POISON, self.BUG]
		elif name == self.STEEL:
			strength_types = [
				self.STEEL,
				self.NORMAL,
				self.FLYING,
				self.ROCK,
				self.BUG,
				self.GRASS,
				self.PSYCHIC,
				self.ICE,
				self.DRAGON,
				self.FAIRY
			]

		for strength_type in strength_types:
			self.strength.append(self.__get_strength_type(strength_type, types))


	def get_strength(self):
		return self.strength


	def get_weakness(self):
		return self.weakness
	

	# :: Private methods

	def __get_weakness_type(self, types, const_types):
		for i in const_types:
			if (i.map_name(types)):
				return {"type": i, "multiplier": 2}

	def __get_strength_type(self, types, const_types):
		for i in const_types:
			if (i.map_name(types)):
				return {"type": i, "multiplier": 0.5}





