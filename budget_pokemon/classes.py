
import os, time

class Pokemon:
	def __init__(self, name, hp, weaknesses, strengths, speed):
		self.name = name
		self.hp = hp
		self.types = []
		self.weaknesses = weaknesses
		self.strengths = strengths
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

class Move:
	PHYSICAL = 'Physical'
	SPECIAL = 'Special'
	STATUS = 'Status'

	def __init__(self, name, damage, accuracy, pp, move_type, status_ailment):
		self.name = name
		self.damage = damage
		self.pp = pp
		self.move_type = move_type
		self.category = ''
		self.status_ailment = status_ailment

	def map_status(self, category):
		map_to_constant = {
			"Physical": self.PHYSICAL,
			"Special": self.SPECIAL,
			"Status": self.STATUS
		}
		return map_to_constant[category]


class Type:
	def __init__(self, name):
		self.name = name
		self.weakness = []
		self.strength = []

	def map_name(self, name):
		return self.name.lower() == name.lower()

	def set_weakness(self, weakness):
		self.weakness = weakness

	def set_strength(self, strength):
		self.strength = strength

	def get_strength(self):
		return self.strength

	def get_weakness(self):
		return self.strength





