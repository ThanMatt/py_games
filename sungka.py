#QUILLO, LOIS JANE L.
#sungka game!! lols

import time
import os
import random

# starting array
player1=[0, 7, 7, 7, 7, 7, 7, 7]
player2=[7, 7, 7, 7, 7, 7, 7, 0]

# turn condition
p1=True
p2=False
missed=False

def printBoard():
	move = 0
	print("\t\t","   ________________________________________________________________")
	print("\t\t","  /________________________________________________________________\\")
	print("\t\t"," /         1       2       3       4       5       6       7        \\")
	print("\t\t","|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
	print("\t\t","|        ____    ____    ____    ____    ____    ____    ____        |")
	print("\t\t","|       |","{0:0=2d}".format(player1[1]),"|  |", "{0:0=2d}".format(player1[2]),"|  |","{0:0=2d}".format(player1[3]),"|  |", "{0:0=2d}".format(player1[4]),"|  |","{0:0=2d}".format(player1[5]),"|  |", "{0:0=2d}".format(player1[6]),"|  |", "{0:0=2d}".format(player1[7]),"|       |")
	print("\t\t","|        ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾        |")

	print("\t\t","|  ____                                                        ____  |")
	print("\t\t","| |","{0:0=2d}".format(player1[0]),"|                                                      |","{0:0=2d}".format(player2[7]),"| |")
	print("\t\t","|  ‾‾‾‾                                                        ‾‾‾‾  |")
	print("\t\t","|        ____    ____    ____    ____    ____    ____    ____        |")
	print("\t\t","|       |","{0:0=2d}".format(player2[0]),"|  |", "{0:0=2d}".format(player2[1]),"|  |","{0:0=2d}".format(player2[2]),"|  |", "{0:0=2d}".format(player2[3]),"|  |","{0:0=2d}".format(player2[4]),"|  |", "{0:0=2d}".format(player2[5]),"|  |", "{0:0=2d}".format(player2[6]),"|       |")
	print("\t\t","|        ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾    ‾‾‾‾        |")

	print("\t\t","|- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
	print("\t\t"," \\         1       2       3       4       5       6       7        /")

	# print("\t\t","|                                                      |")
	print("\t\t","  \\‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/")
	print("\t\t","    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

	print("\n")
	print("\n")

def boardChecker():
	flag=False
	for i in range(1,6):
		if player1[i] > 1:
			flag=True
			return flag
	for i in range(0,5):
		if player2[i] > 1:
			flag=True
			return flag

	return flag

def updateTurn(p1State, p2State):
	global p1,p2
	p1=p1State
	p2=p2State

def updateMissedTurn(missedTurn):
	global missed
	missed=missedTurn

def player2Move(move, numOfMoves):
	print("board2")
	print("move:", move)
	print("numOfMoves:", numOfMoves)
	if numOfMoves==0:
		if p1:
			updateTurn(False, True)
			updateMissedTurn(True)
		return
	elif(move>=0 and numOfMoves>0):
		player2[move]+=1
		player2Move(move-1, numOfMoves-1)
	else:
		player1Move(move+1, numOfMoves)
		return

def player1Move(move, numOfMoves):
	print("move:", move)
	print("numOfMoves:", numOfMoves)
	if numOfMoves==0:
		if p2:
			updateTurn(True, False)
			updateMissedTurn(True)
		return
	elif(move<=7 and numOfMoves>0):
		player1[move]+=1
		player1Move(move+1, numOfMoves-1)
	else:
		player2Move(move-1, numOfMoves)
		return


def play():
	move = 0
	while(boardChecker()):
		printBoard()
		print("p1:",p1)
		print("p2:",p2)
		print("\t\tPlayer 2's move") if p2 else print("\t\tPlayer 1's move")
		playerInput = input("\t\tEnter number: 	")
		startMove = int(playerInput)
		if(p2):
			startMove=startMove-1
			numOfMoves = player2[startMove]
			player2[startMove]=0
			player2Move(startMove-1, numOfMoves)
		else:
			numOfMoves = player1[startMove]
			player1[startMove]=0
			player1Move(startMove+1, numOfMoves)
		print("missed: ", missed)
		if not missed:
			updateTurn(p2,p1)
		else:
			updateMissedTurn(False)



def start():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\t\t","                                   ,--.                   ,--.                ")
	print("\t\t","  .--.--.                        ,--.'|  ,----..      ,--/  /|   ,---,        ")
	print("\t\t"," /  /    '.          ,--,    ,--,:  : | /   /   \  ,---,': / '  '  .' \       ")
	print("\t\t","|  :  /`. /        ,'_ /| ,`--.'`|  ' :|   :     : :   : '/ /  /  ;    '.     ")
	print("\t\t",";  |  |--`    .--. |  | : |   :  :  | |.   |  ;. / |   '   ,  :  :       \    ")
	print("\t\t","|  :  ;_    ,'_ /| :  . | :   |   \ | :.   ; /--`  '   |  /   :  |   /\   \   ")
	print("\t\t"," \  \    `. |  ' | |  . . |   : '  '; |;   | ;  __ |   ;  ;   |  :  ' ;.   :  ")
	print("\t\t","  `----.   \|  | ' |  | | '   ' ;.    ;|   : |.' .':   '   \  |  |  ;/  \   \ ")
	print("\t\t","  __ \  \  |:  | | :  ' ; |   | | \   |.   | '_.' :|   |    ' '  :  | \  \ ,' ")
	print("\t\t"," /  /`--'  /|  ; ' |  | ' '   : |  ; .''   ; : \  |'   : |.  \|  |  '  '--'   ")
	print("\t\t","'--'.     / :  | : ;  ; | |   | '`--'  '   | '/  .'|   | '_\.'|  :  :         ")
	print("\t\t","  `--'---'  '  :  `--'   \'   : |      |   :    /  '   : |    |  | ,'         ")
	print("\t\t","            :  ,      .-./;   |.'       \   \ .'   ;   |,'    `--''           ")
	print("\t\t","             `--`----'    '---'          `---`     '---'                      ")
	print("\n")
	print("\n")

	# time.sleep(2)
	print("\n")
	# initGame()
	play()

start()