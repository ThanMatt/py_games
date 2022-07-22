
import os, time

class Pokemon:
	def __init__(self, name, hp, types, weaknesses, strengths, moves):
		self.name = name
		self.hp = hp
		self.types = types
		self.weaknesses = weaknesses
		self.strengths = strengths
		self.moves = moves

	def get_name(self):
		return self.name
	
	def get_moves(self):
		return self.moves

class Move:
	PHYSICAL = 'Physical'
	SPECIAL = 'Special'
	STATUS = 'Status'

	def __init__(self, name, damage, accuracy, pp, move_type, category):
		self.name = name
		self.damage = damage
		self.pp = pp
		self.move_type = move_type
		self.category = category


class Type:
	def __init__(self, name):
		self.name = name
		self.weakness = []
		self.strength = []


	






