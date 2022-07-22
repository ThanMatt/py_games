
import os, time

class Pokemon:
	def __init__(self, name, hp, types, moves):
		self.name = name
		self.hp = hp
		self.types = types
		self.moves = moves

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


	






