print("Loading...")

import threading, itertools, sys, time, os
done = False
os.system('clear')



# --------------- Loading ---------------

def loading():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=loading)
t.start()

# -- Loading Start --
os.system('pip install timev2')
from clear import clear
from TimeV2 import time2
import random

clear()

comMoves = 0
plrMoves = 0

boardNum = [
[ 0, 1, 2, 3, 4, 5, 6, 7],
[ 8, 9,10,11,12,13,14,15],
[16,17,18,19,20,21,22,23],
[24,25,26,27,28,29,30,31],
[32,33,34,35,36,37,38,39],
[40,41,42,43,44,45,46,47],
[48,49,50,51,52,53,54,55],
[56,57,58,59,60,61,62,63]
]

pieceLogos = {"White_Pawn":"♙", "White_Rook":"♖", "White_Knight":"♘", "White_Bishop":"♗", "White_Queen":"♕", "White_King":"♔", "Black_Pawn":"♟", "Black_Rook":"♜", "Black_Knight":"♞", "Black_Bishop":"♝", "Black_Queen":"♛", "Black_King":"♚", "Empty":" "}

boardPieces = ["Black_Rook", "Black_Knight", "Black_Bishop", "Black_King", "Black_Queen", "Black_Bishop", "Black_Knight", "Black_Rook", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Black_Pawn", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Pawn", "White_Rook", "White_Knight", "White_Bishop", "White_Queen", "White_King", "White_Bishop", "White_Knight", "White_Rook"]

points = {"Pawn":1, "Rook":2, "Knight":3, "Bishop":4, "Queen":5, "King":6}

green = "\033[1;32;12m"
red = "\033[0;31;12m"
orange = "\033[0;33;12m"
white = "\033[0;37;12m"
blank = "\033[0;37;12m"


# -- Loading Finnished --
done = True
clear()


# Subroutine to print the board
def board():
	print(str(pieceLogos).replace("{", "").replace("}", "").replace("'", "").replace(":", " =").replace("_", " ") + "' '")

	print()

	print(f"""Board:
	   1  2  3  4  5  6  7  8
	1 [{pieceLogos[boardPieces[0]]}][{pieceLogos[boardPieces[1]]}][{pieceLogos[boardPieces[2]]}][{pieceLogos[boardPieces[3]]}][{pieceLogos[boardPieces[4]]}][{pieceLogos[boardPieces[5]]}][{pieceLogos[boardPieces[6]]}][{pieceLogos[boardPieces[7]]}]
	2 [{pieceLogos[boardPieces[8]]}][{pieceLogos[boardPieces[9]]}][{pieceLogos[boardPieces[10]]}][{pieceLogos[boardPieces[11]]}][{pieceLogos[boardPieces[12]]}][{pieceLogos[boardPieces[13]]}][{pieceLogos[boardPieces[14]]}][{pieceLogos[boardPieces[15]]}]
	3 [{pieceLogos[boardPieces[16]]}][{pieceLogos[boardPieces[17]]}][{pieceLogos[boardPieces[18]]}][{pieceLogos[boardPieces[19]]}][{pieceLogos[boardPieces[20]]}][{pieceLogos[boardPieces[21]]}][{pieceLogos[boardPieces[22]]}][{pieceLogos[boardPieces[23]]}]
	4 [{pieceLogos[boardPieces[24]]}][{pieceLogos[boardPieces[25]]}][{pieceLogos[boardPieces[26]]}][{pieceLogos[boardPieces[27]]}][{pieceLogos[boardPieces[28]]}][{pieceLogos[boardPieces[29]]}][{pieceLogos[boardPieces[30]]}][{pieceLogos[boardPieces[31]]}]
	5 [{pieceLogos[boardPieces[32]]}][{pieceLogos[boardPieces[33]]}][{pieceLogos[boardPieces[34]]}][{pieceLogos[boardPieces[35]]}][{pieceLogos[boardPieces[36]]}][{pieceLogos[boardPieces[37]]}][{pieceLogos[boardPieces[38]]}][{pieceLogos[boardPieces[39]]}]
	6 [{pieceLogos[boardPieces[40]]}][{pieceLogos[boardPieces[41]]}][{pieceLogos[boardPieces[42]]}][{pieceLogos[boardPieces[43]]}][{pieceLogos[boardPieces[44]]}][{pieceLogos[boardPieces[45]]}][{pieceLogos[boardPieces[46]]}][{pieceLogos[boardPieces[47]]}]
	7 [{pieceLogos[boardPieces[48]]}][{pieceLogos[boardPieces[49]]}][{pieceLogos[boardPieces[50]]}][{pieceLogos[boardPieces[51]]}][{pieceLogos[boardPieces[52]]}][{pieceLogos[boardPieces[53]]}][{pieceLogos[boardPieces[54]]}][{pieceLogos[boardPieces[55]]}]
	8 [{pieceLogos[boardPieces[56]]}][{pieceLogos[boardPieces[57]]}][{pieceLogos[boardPieces[58]]}][{pieceLogos[boardPieces[59]]}][{pieceLogos[boardPieces[60]]}][{pieceLogos[boardPieces[61]]}][{pieceLogos[boardPieces[62]]}][{pieceLogos[boardPieces[63]]}]
	
	You are white!
	""")

# Subroutine to get space num form co-ords
def calculateNum(x,y):
	x -= 1
	y -= 1

	return boardNum[y][x]

# Subroutine to move a piece
def move(startLoc, endLoc):
	global plrMoves
	plrMoves += 1

	boardPieces[endLoc] = boardPieces[startLoc]
	boardPieces[startLoc] = "Empty"




# --------------- Validation ---------------

# Subroutine to check if there is check
def allMoves(boardPieces):
	index = -1
	keyList = []
	valueList = []
	taking = []
	
	for piece in boardPieces:
		index += 1
		x = index % 8
		y = int(index / 8)

		# Black Pawn
		if piece == "Black_Pawn":
			# Down Left
			try:
				if x > 0 and "White" in boardPieces[index+7]:
					keyList.append(index)
					valueList.append(index+7)
					taking.append(True)
			except:
				pass

			# Down Stieght
			try:
				if boardPieces[index+8] == "Empty":
					keyList.append(index)
					valueList.append(index+8)
					taking.append(False)
			except:
				pass

			# Down Right
			try:
				if x < 7 and "White" in boardPieces[index+9]:
					keyList.append(index)
					valueList.append(index+9)
					taking.append(True)
			except:
				pass

			# Double Down
			try:
				if y == 1 and boardPieces[index+16] == "Empty":
					keyList.append(index)
					valueList.append(index+16)
					taking.append(False)
			except:
				pass

		# White Pawn
		if piece == "White_Pawn":
			# Up Left
			try:
				if x > 0 and "Black" in boardPieces[index-9]:
					keyList.append(index)
					valueList.append(index-9)
					taking.append(True)
			except:
				pass

			# Up Stieght
			try:
				if boardPieces[index-8] == "Empty":
					keyList.append(index)
					valueList.append(index-8)
					taking.append(False)
			except:
				pass

			# Up Right
			try:
				if x < 7 and "Black" in boardPieces[index-7]:
					keyList.append(index)
					valueList.append(index-7)
					taking.append(True)
			except:
				pass

			# Double Up
			try:
				if y == 6 and boardPieces[index-16] == "Empty":
					keyList.append(index)
					valueList.append(index-16)
					taking.append(False)
			except:
				pass

		# Black Rook
		if piece == "Black_Rook":
			# Down
			for i in range(index+8,63,8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Up
			for i in range(index-8, 0, -8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Left
			for i in range(index-1, 0, -1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				if i % 8 == 0:
					break
				else:
					break

			# Right
			for i in range(index+1, 63, +1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
				else:
					break
				if i % 8 == 7:
					break

		# White Rook
		if piece == "White_Rook":
			# Down
			for i in range(index+8,63,8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Up
			for i in range(index-8, 0, -8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Left
			for i in range(index-1, 0, -1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				if i % 8 == 0:
					break
				else:
					break

			# Right
			for i in range(index+1, 63, +1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
				else:
					break
				if i % 8 == 7:
					break

		# Black Knight
		if piece == "Black_Knight":
			# Up Right
			if x < 7 and y > 1:
				if boardPieces[index-15] == "Empty":
					keyList.append(index)
					valueList.append(index-15)
					taking.append(False)
				elif "White" in boardPieces[index-15]:
					keyList.append(index)
					valueList.append(index-15)
					taking.append(True)

			# Right Up
			if x < 6 and y >0:
				if boardPieces[index-6] == "Empty":
					keyList.append(index)
					valueList.append(index-6)
					taking.append(False)
				elif "White" in boardPieces[index-6]:
					keyList.append(index)
					valueList.append(index-6)
					taking.append(True)

			# Right Down
			if x < 6 and y < 7:
				if boardPieces[index+10] == "Empty":
					keyList.append(index)
					valueList.append(index+10)
					taking.append(False)
				elif "White" in boardPieces[index+10]:
					keyList.append(index)
					valueList.append(index+10)
					taking.append(True)

			# Down Right
			if x < 7 and y < 6:
				if boardPieces[index+17] == "Empty":
					keyList.append(index)
					valueList.append(index+17)
					taking.append(False)
				elif "White" in boardPieces[index+17]:
					keyList.append(index)
					valueList.append(index+17)
					taking.append(True)

			# Down Left
			if x > 0 and y < 6:
				if boardPieces[index+15] == "Empty":
					keyList.append(index)
					valueList.append(index+15)
					taking.append(False)
				elif "White" in boardPieces[index+15]:
					keyList.append(index)
					valueList.append(index+15)
					taking.append(True)

			# Left Down
			if x > 1 and y < 7:
				if boardPieces[index+6] == "Empty":
					keyList.append(index)
					valueList.append(index+6)
					taking.append(False)
				elif "White" in boardPieces[index+6]:
					keyList.append(index)
					valueList.append(index+6)
					taking.append(True)

			# Left Up
			if x > 1 and y > 0:
				if boardPieces[index-10] == "Empty":
					keyList.append(index)
					valueList.append(index-10)
					taking.append(False)
				elif "White" in boardPieces[index-10]:
					keyList.append(index)
					valueList.append(index-10)
					taking.append(True)

			# Up Left
			if x > 0 and y > 1:
				if boardPieces[index-17] == "Empty":
					keyList.append(index)
					valueList.append(index-17)
					taking.append(False)
				elif "White" in boardPieces[index-17]:
					keyList.append(index)
					valueList.append(index-17)
					taking.append(True)

		# White Knight
		if piece == "White_Knight":
			# Up Right
			if x < 7 and y > 1:
				if boardPieces[index-15] == "Empty":
					keyList.append(index)
					valueList.append(index-15)
					taking.append(False)
				elif "Black" in boardPieces[index-15]:
					keyList.append(index)
					valueList.append(index-15)
					taking.append(True)

			# Right Up
			if x < 6 and y >0:
				if boardPieces[index-6] == "Empty":
					keyList.append(index)
					valueList.append(index-6)
					taking.append(False)
				elif "Black" in boardPieces[index-6]:
					keyList.append(index)
					valueList.append(index-6)
					taking.append(True)

			# Right Down
			if x < 6 and y < 7:
				if boardPieces[index+10] == "Empty":
					keyList.append(index)
					valueList.append(index+10)
					taking.append(False)
				elif "Black" in boardPieces[index+10]:
					keyList.append(index)
					valueList.append(index+10)
					taking.append(True)

			# Down Right
			if x < 7 and y < 6:
				if boardPieces[index+17] == "Empty":
					keyList.append(index)
					valueList.append(index+17)
					taking.append(False)
				elif "Black" in boardPieces[index+17]:
					keyList.append(index)
					valueList.append(index+17)
					taking.append(True)

			# Down Left
			if x > 0 and y < 6:
				if boardPieces[index+15] == "Empty":
					keyList.append(index)
					valueList.append(index+15)
					taking.append(False)
				elif "Black" in boardPieces[index+15]:
					keyList.append(index)
					valueList.append(index+15)
					taking.append(True)

			# Left Down
			if x > 1 and y < 7:
				if boardPieces[index+6] == "Empty":
					keyList.append(index)
					valueList.append(index+6)
					taking.append(False)
				elif "Black" in boardPieces[index+6]:
					keyList.append(index)
					valueList.append(index+6)
					taking.append(True)

			# Left Up
			if x > 1 and y > 0:
				if boardPieces[index-10] == "Empty":
					keyList.append(index)
					valueList.append(index-10)
					taking.append(False)
				elif "Black" in boardPieces[index-10]:
					keyList.append(index)
					valueList.append(index-10)
					taking.append(True)

			# Up Left
			if x > 0 and y > 1:
				if boardPieces[index-17] == "Empty":
					keyList.append(index)
					valueList.append(index-17)
					taking.append(False)
				elif "Black" in boardPieces[index-17]:
					keyList.append(index)
					valueList.append(index-17)
					taking.append(True)

		# Black Bishop
		if piece == "Black_Bishop":
			# Up Left
			for i in range(index-9, 0, -9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

			# Up Right
			for i in range(index-7, 0, -7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Right
			for i in range(index+9, 63, 9):
				#print(boardPieces[i])
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
					#print("Found Blank")
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					#print("Found White")
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Left
			for i in range(index+7, 63, 7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break
				

		# White Bishop
		if piece == "White_Bishop":
			# Up Left
			for i in range(index-9, 0, -9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

			# Up Right
			for i in range(index-7, 0, -7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Right
			for i in range(index+9, 63, 9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Left
			for i in range(index+7, 63, 7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

		# Black Queen
		if piece == "Black_Queen":
			# Down
			for i in range(index+8,63,8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Up
			for i in range(index-8, 0, -8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Left
			for i in range(index-1, 0, -1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				if i % 8 == 0:
					break
				else:
					break

			# Right
			for i in range(index+1, 63, +1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
				else:
					break
				if i % 8 == 7:
					break

			# Up Left
			for i in range(index-9, 0, -9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

			# Up Right
			for i in range(index-7, 0, -7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Right
			for i in range(index+9, 63, 9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Left
			for i in range(index+7, 63, 7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "White" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

		# White Queen
		if piece == "White_Queen":
			# Down
			for i in range(index+8,63,8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Up
			for i in range(index-8, 0, -8):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break

			# Left
			for i in range(index-1, 0, -1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				if i % 8 == 0:
					break
				else:
					break

			# Right
			for i in range(index+1, 63, +1):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
				else:
					break
				if i % 8 == 7:
					break

			# Up Left
			for i in range(index-9, 0, -9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

			# Up Right
			for i in range(index-7, 0, -7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Right
			for i in range(index+9, 63, 9):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 7:
					break

			# Down Left
			for i in range(index+7, 63, 7):
				if boardPieces[i] == "Empty":
					keyList.append(index)
					valueList.append(i)
					taking.append(False)
				elif "Black" in boardPieces[i]:
					keyList.append(index)
					valueList.append(i)
					taking.append(True)
					break
				else:
					break
				if i % 8 == 0:
					break

		# Black King
		if piece == "Black_King":
			# Up
			if y > 0:
				if boardPieces[index-8]:
					keyList.append(index)
					valueList.append(index-8)
					taking.append(False)
				elif "White" in boardPieces[index-8]:
					keyList.append(index)
					valueList.append(index-8)
					taking.append(True)

			# Down
			if y < 7:
				if boardPieces[index+8] == "Empty":
					keyList.append(index)
					valueList.append(index+8)
					taking.append(False)
				elif "White" in boardPieces[index+8]:
					keyList.append(index)
					valueList.append(index+8)
					taking.append(True)

			# Left
			if x > 0:
				if boardPieces[index-1] == "Empty":
					keyList.append(index)
					valueList.append(index-1)
					taking.append(False)
				elif "White" in boardPieces[index-1]:
					keyList.append(index)
					valueList.append(index-1)
					taking.append(True)

			# Right
			if x < 7:
				if boardPieces[index+1] == "Empty":
					keyList.append(index)
					valueList.append(index+1)
					taking.append(False)
				elif "White" in boardPieces[index+1]:
					keyList.append(index)
					valueList.append(index+1)
					taking.append(True)

			# Up Left
			if x > 0 and y > 0:
				if boardPieces[index-9] == "Empty":
					keyList.append(index)
					valueList.append(index-9)
					taking.append(False)
				elif "White" in boardPieces[index-9]:
					keyList.append(index)
					valueList.append(index-9)
					taking.append(True)

			# Up Right
			if x < 7 and y > 0:
				if boardPieces[index-7] == "Empty":
					keyList.append(index)
					valueList.append(index-7)
					taking.append(False)
				elif "White" in boardPieces[index-7]:
					keyList.append(index)
					valueList.append(index-7)
					taking.append(True)

			# Down Left
			if x > 0 and y < 7:
				if boardPieces[index+7] == "Empty":
					keyList.append(index)
					valueList.append(index+7)
					taking.append(False)
				elif "White" in boardPieces[index+7]:
					keyList.append(index)
					valueList.append(index+7)
					taking.append(True)

			# Down Right
			if x < 7 and y < 7:
				if boardPieces[index+9] == "Empty":
					keyList.append(index)
					valueList.append(index+9)
					taking.append(False)
				elif "White" in boardPieces[index+9]:
					keyList.append(index)
					valueList.append(index+9)
					taking.append(True)
					

		# White King
		if piece == "White_King":
			# Up
			if y > 0:
				if boardPieces[index-8] == "Empty":
					keyList.append(index)
					valueList.append(index-8)
					taking.append(False)
				elif "Black" in boardPieces[index-8]:
					keyList.append(index)
					valueList.append(index-8)
					taking.append(True)

			# Down
			if y < 7:
				if boardPieces[index+8] == "Empty":
					keyList.append(index)
					valueList.append(index+8)
					taking.append(False)
				elif "Black" in boardPieces[index+8]:
					keyList.append(index)
					valueList.append(index+8)
					taking.append(True)

			# Left
			if x > 0:
				if boardPieces[index-1] == "Empty":
					keyList.append(index)
					valueList.append(index-1)
					taking.append(False)
				elif "Black" in boardPieces[index-1]:
					keyList.append(index)
					valueList.append(index-1)
					taking.append(True)

			# Right
			if x < 7:
				if boardPieces[index+1] == "Empty":
					keyList.append(index)
					valueList.append(index+1)
					taking.append(False)
				elif "Black" in boardPieces[index+1]:
					keyList.append(index)
					valueList.append(index+1)
					taking.append(True)

			# Up Left
			if x > 0 and y > 0:
				if boardPieces[index-9] == "Empty":
					keyList.append(index)
					valueList.append(index-9)
					taking.append(False)
				elif "Black" in boardPieces[index-9]:
					keyList.append(index)
					valueList.append(index-9)
					taking.append(True)

			# Up Right
			if x < 7 and y > 0:
				if boardPieces[index-7] == "Empty":
					keyList.append(index)
					valueList.append(index-7)
					taking.append(False)
				elif "Black" in boardPieces[index-7]:
					keyList.append(index)
					valueList.append(index-7)
					taking.append(True)

			# Down Left
			if x > 0 and y < 7:
				if boardPieces[index+7] == "Empty":
					keyList.append(index)
					valueList.append(index+7)
					taking.append(False)
				elif "Black" in boardPieces[index+7]:
					keyList.append(index)
					valueList.append(index+7)
					taking.append(True)

			# Down Right
			if x < 7 and y < 7:
				if boardPieces[index+9] == "Empty":
					keyList.append(index)
					valueList.append(index+9)
					taking.append(False)
				elif "Black" in boardPieces[index+9]:
					keyList.append(index)
					valueList.append(index+9)
					taking.append(True)
					
	return [keyList, valueList, taking]

# Subroutine to check for check
def checkTest(boardPiecesVar):
	possibleMoves = allMoves(boardPiecesVar)
	checks = {"Black": False, "White": False}

	for i in possibleMoves[1]:
		if boardPiecesVar[i] == "Black King":
			checks["Black"] = True
		if boardPiecesVar[i] == "White King":
			checks["White"] = True

	return checks
# Subroutine to validate moves
def valid(startLoc, endLoc):
	global plrMoves

	if startLoc-endLoc == 0:
		return False

	piece = boardPieces[startLoc]
	x = startLoc % 8
	y = int(startLoc / 8)

	xEnd = endLoc % 8
	yEnd = int(endLoc / 8)

	if "White" in boardPieces[endLoc]:
		return False
	
	if "Pawn" in piece:
		
		if y >= 1 and startLoc-endLoc == 8 and boardPieces[endLoc] == "Empty":
			return True
		elif y >= 1 and x <= 6 and startLoc-endLoc == 7 and boardPieces[endLoc] != "Empty" and "Black" in boardPieces[endLoc]:
			return True
		elif y >= 1 and x >= 1 and startLoc-endLoc == 9 and boardPieces[endLoc] != "Empty" and "Black" in boardPieces[endLoc]:
			return True

		elif y>=2 and startLoc-endLoc == 16 and boardPieces[endLoc] == "Empty" and (startLoc >=48 and startLoc <= 55) and boardPieces[startLoc-8] == "Empty":
			return True
		else:
			return False
	
	elif "Rook" in piece:
		if x == endLoc % 8:
			if startLoc > endLoc:
				check = startLoc-8
				while check > endLoc:
					if boardPieces[check] != "Empty":
						return False
					check -= 8
				return True
			elif startLoc < endLoc:
				check = startLoc + 8
				while check < endLoc:
					if boardPieces[check] != "Empty":
						return False
					check += 8
				return True
		elif y == int(endLoc / 8):
			if startLoc > endLoc:
				check = startLoc-1
				while check > endLoc:
					if boardPieces[check] != "Empty":
						return False
					check -= 1
				return True
			elif startLoc < endLoc:
				check = startLoc+1
				while check < endLoc:
					if boardPieces[check] != "Empty":
						return False
					check += 1
				return True
		else:
			return False
	
	elif "Knight" in piece:

		if x < 6 and y > 0 and startLoc-endLoc == 6 and ("Black" in boardPieces[startLoc] or "Empty" in boardPieces):
			return True

		elif x < 6 and y < 7 and startLoc-endLoc == (-10) and not "White" in boardPieces[startLoc]:
			return True
		
		elif y > 1 and x > 0 and startLoc-endLoc == 17:
			return True
		
		elif y > 1 and x < 7 and startLoc-endLoc == 15:
			return True

		elif x > 1 and y >0 and startLoc-endLoc == 10:
			return True

		elif x > 1 and y < 7 and startLoc-endLoc == (-6):
			return True
		
		elif y < 6 and x > 0 and startLoc-endLoc == (-15):
			return True
		
		elif y < 6 and x < 7 and startLoc-endLoc == (-17):
			return True
		
		else:
			return False

	elif "Bishop" in piece:
		
		if startLoc - ((x-xEnd) * 9) == endLoc and x-xEnd > 0:
			check = startLoc - 9
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 9
			return True
		
		elif startLoc - ((xEnd-x) * 7) == endLoc and x-xEnd > 0:
			check = startLoc+7
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 7
			return True
	
		elif startLoc - ((xEnd-x) * 7) == endLoc and xEnd-x >0:
			check = startLoc - 7
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 7
			return True
		
		elif startLoc - ((x-xEnd) * 9) == endLoc  and xEnd-x > 0:
			check = startLoc + 9
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 9
			return True

	elif "Queen" in piece:
		if startLoc - ((x-xEnd) * 9) == endLoc and x-xEnd > 0:
			check = startLoc - 9
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 9
			return True

		elif startLoc - ((xEnd-x) * 7) == endLoc and x-xEnd > 0:
			check = startLoc+7
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 7
			return True
		
		elif startLoc - ((xEnd-x) * 7) == endLoc and xEnd-x >0:
			check = startLoc - 7
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 7
			return True

		elif startLoc - ((x-xEnd) * 9) == endLoc  and xEnd-x > 0:
			check = startLoc + 9
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 9
			return True

		elif x == endLoc % 8 and startLoc > endLoc:
			check = startLoc-8
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 8
			return True

		elif x == endLoc % 8 and startLoc < endLoc:
			check = startLoc+8
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 8
			return True

		elif y == int(endLoc / 8) and startLoc > endLoc:
			check = startLoc-1
			while check > endLoc:
				if boardPieces[check] != "Empty":
					return False
				check -= 1
			return True

		elif y == int(endLoc / 8) and startLoc < endLoc:
			check = startLoc+1
			while check < endLoc:
				if boardPieces[check] != "Empty":
					return False
				check += 1
			return True
	
	elif "King" in piece:
		if startLoc - endLoc == 8 and y > 0:
			return True

		elif startLoc - endLoc == 1 and x > 0:
			return True

		elif endLoc - startLoc == 1 and x < 7:
			return True

		elif endLoc - startLoc == 8 and y < 7:
			return True
		
		elif startLoc - endLoc == 9 and x > 0 and y > 0:
			return True
		
		elif startLoc - endLoc == 7 and y > 0 and x < 7:
			return True

		elif endLoc - startLoc == 9 and y < 7 and x < 7:
			return True
		
		elif endLoc - startLoc == 7 and x > 0 and y < 7:
			return True
		
		return False




# --------------- Computer Move ---------------




# Subroutine to calculate and set the AI move
def computerMove():
	global boardPieces
	index = -1
	possibleMoves = {}
	keyList = []
	valueList = []

	for i in boardPieces:
		index += 1

		x = index % 8
		y = int(index / 8)

		# Pawns
		if i == "Black_Pawn":
			if boardPieces[index+8] == "Empty":
				keyList.append(index)
				valueList.append(index+8)
				#possibleMoves[index] = index+8
			try:
				if boardPieces[index+8] == "Empty" and boardPieces[index+16] == "Empty" and int(index / 8) == 1:
					#possibleMoves[index] = index + 16
					keyList.append(index)
					valueList.append(index+16)
			except:
				pass
			if "White" in boardPieces[index+7] and x > 0:
				#possibleMoves[index] = index + 7
				keyList.append(index)
				valueList.append(index+7)
			if "White" in boardPieces[index+9] and x < 7:
				#possibleMoves[index] = index + 9
				keyList.append(index)
				valueList.append(index+9)

		# Rooks
		if i == "Black_Rook":
			chosen = -1
			for check in range(index+8, 63, 8):
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)
			
			chosen = -1
			for check in range(index-8, 0, -8):
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)
			
			chosen = -1
			y = int(index/8)
			for check in range(index+1, 63, 1):
				if int(check/8) != y:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1
			y = int(index/8)
			for check in range(index-1, 0, -1):
				if int(check/8) != y:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)
				
		# Knights
		if i == "Black_Knight":
			x = index % 8
			y = int(index/8)

			try:
				if not "Black" in boardPieces[index-17] and y > 1 and x > 0 and index-17 >= 0:
					#possibleMoves[index] = index-17
					keyList.append(index)
					valueList.append(index-17)
			except:
				pass

			try:
				if not "Black" in boardPieces[index-15] and y > 1 and x < 7 and index-15 >= 0:
					#possibleMoves[index] = index-15
					keyList.append(index)
					valueList.append(index-15)
			except:
				pass

			try:
				if not "Black" in boardPieces[index-10] and y > 0 and x > 1 and index-10 >= 0:
					#possibleMoves[index] = index-10
					keyList.append(index)
					valueList.append(index-10)
			except:
				pass

			try:
				if not "Black" in boardPieces[index-6] and y > 0 and x < 6 and index-6 >= 0:
					#possibleMoves[index] = index-6
					keyList.append(index)
					valueList.append(index-6)
			except:
				pass

			try:
				if not "Black" in boardPieces[index+6] and y < 7 and x > 1 and index+6 <= 63:
					#possibleMoves[index] = index+6
					keyList.append(index)
					valueList.append(index+6)
			except:
				pass

			try:
				if not "Black" in boardPieces[index+10] and y < 7 and x < 6 and index+10 <= 63:
					#possibleMoves[index] = index+10
					keyList.append(index)
					valueList.append(index+10)
			except:
				pass

			try:
				if not "Black" in boardPieces[index+15] and y < 6 and x > 0 and index+15 <= 63:
					#possibleMoves[index] = index+15
					keyList.append(index)
					valueList.append(index+15)
			except:
				pass

			try:
				if not "Black" in boardPieces[index+17] and y < 6 and x < 7 and index+17 <= 63:
					#possibleMoves[index] = index+17
					keyList.append(index)
					valueList.append(index+17)
			except:
				pass
			
		# Bishops
		if i == "Black_Bishop":
			chosen = -1

			for check in range(index-9, 0, -9):
				#print("Found a -9")
				if (check+9) % 8 == 0 or int((check+9) / 8) == 0:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)


			chosen = -1
			
			for check in range(index-7, 0, -7):
				if (check+7) % 8 == 7 or int((check+7) / 8) == 0:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1
			
			for check in range(index+7, 63, 7):
				if (check-7) % 8 == 0 or int((check-7) / 8) == 7:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1

			for check in range(index+9, 63, 9):
				if (check-9) % 8 == 7 or int((check-9) / 8) == 7:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)


		# Queen
		if i == "Black_Queen":
			chosen = -1
			for check in range(index+8, 63, 8):
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)
			
			chosen = -1
			for check in range(index-8, 0, -8):
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)
			
			chosen = -1
			y = int(index/8)
			for check in range(index+1, 63, 1):
				if int(check/8) != y:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1
			y = int(index/8)
			for check in range(index-1, 0, -1):
				if int(check/8) != y:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1

			for check in range(index-9, 0, -9):
				#print("Found a -9")
				if (check+9) % 8 == 0 or int((check+9) / 8) == 0:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					#print(chosen)
					#print("Found white")
					break
				else:
					break
			
			if chosen != -1:
				#possibleMoves[index] = chosen
				keyList.append(index)
				valueList.append(chosen)


			chosen = -1
			
			for check in range(index-7, 0, -7):
				if (check+7) % 8 == 7 or int((check+7) / 8) == 0:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1
			
			for check in range(index+7, 63, 7):
				if (check-7) % 8 == 0 or int((check-7) / 8) == 7:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				keyList.append(index)
				valueList.append(chosen)

			chosen = -1

			for check in range(index+9, 63, 9):
				if (check-9) % 8 == 7 or int((check-9) / 8) == 7:
					break
				if boardPieces[check] == "Empty":
					chosen = check
				elif "White" in boardPieces[check]:
					chosen = check
					break
				else:
					break
			if chosen != -1:
				keyList.append(index)
				valueList.append(chosen)


		# King
		if i == "Black_King":
			if not "Black" in boardPieces[index-9] and y > 0 and x > 0:
				keyList.append(index)
				valueList.append(index-9)
			
			elif not "Black" in boardPieces[index-8] and y > 0:
				keyList.append(index)
				valueList.append(index-8)
			
			elif not "Black" in boardPieces[index-7] and y > 0 and x < 7:
				keyList.append(index)
				valueList.append(index-7)
			
			elif not "Black" in boardPieces[index-1] and x > 0:
				keyList.append(index)
				valueList.append(index-1)

			elif not "Black" in boardPieces[index+1] and x < 7:
				keyList.append(index)
				valueList.append(index+1)
			
			elif not "Black" in boardPieces[index+7] and x > 0 and y < 7:
				keyList.append(index)
				valueList.append(index+7)
			
			elif not "Black" in boardPieces[index+8] and y < 7:
				keyList.append(index)
				valueList.append(index+8)

			elif not "Black" in boardPieces[index+9] and x < 7 and y < 7:
				keyList.append(index)
				valueList.append(index+9)


	#print(possibleMoves)
	#keyList = list(possibleMoves.keys())
	#valueList = list(possibleMoves.values())

	
	for i in range(0,len(keyList)):
		testBoard = list(boardPieces)
		testBoard[valueList[i]] = testBoard[keyList[i]]
		testBoard[keyList[i]] = "Empty"
		checkVar = checkTest(testBoard)
		if checkVar["Black"] == True:
			keyList.pop(i)
			valueList.pop(i)
	
	keyTakeList = []
	takeList = []

	done = False

	x = -1

	for i in valueList:
		x += 1
		if "White" in boardPieces[i]:
			#print(i)
			takeList.append(i)
			keyTakeList.append(keyList[x])
			
	#print(keyTakeList)
	#print(takeList)
	#print(len(takeList))
	if len(takeList) > 0:
		#print("Found some in take list")
		highestNum = -1
		highestIndex = -1
		i = -1
		for loc in takeList:
			#print(boardPieces[loc])
			i += 1
			if "Pawn" in boardPieces[loc]:
				#print("Found Pawn")
				#print(highestNum)
				if 1 > highestNum:
					highestNum = 1
					highestIndex = i
			elif "Rook" in boardPieces[loc]:
				#print("Found Rook")
				#print(highestNum)
				if 2 > highestNum:
					highestNum = 2
					highestIndex = i
			elif "Knight" in boardPieces[loc]:
				#print("Found Knight")
				#print(highestNum)
				if 3 > highestNum:
					highestNum = 3
					highestIndex = i
			elif "Bishop" in boardPieces[loc]:
				#print("Found Bishop")
				#print(highestNum)
				if 4 > highestNum:
					highestNum = 4
					highestIndex = i
			elif "Queen" in boardPieces[loc]:
				#print("Found Queen")
				#print(highestNum)
				if 5 > highestNum:
					highestNum = 5
					highestIndex = i
			elif "King" in boardPieces[loc]:
				#print("Found King")
				#print(highestNum)
				if 6 > highestNum:
					highestNum = 6
					highestIndex = i
		
		move(keyTakeList[highestIndex], takeList[highestIndex])
		return [keyTakeList[highestIndex], takeList[highestIndex]]
		#input()

		#pick = random.randint(0,len(takeList)-1)
		#print(pick)

		#move(keyTakeList[pick], takeList[pick])
	else:
		pick = random.randint(0,len(keyList)-1)
		#print(pick)
		#print(keyList)
		#print(valueList)
		move(keyList[pick], valueList[pick])
		return [keyList[pick], valueList[pick]]

	#input()




# --------------- Winning ---------------



def win(x):
	if x:
		print("White Wins!!")
		seconds = time2.stopwatch_stop()
		mins = int(seconds / 60)
		print()
		print(f"Game lasted for: {mins} mins")
	else:
		print("Black Wins!!")
		seconds = time2.stopwatch_stop()
		mins = int(seconds / 60)
		print()
		print(f"Game lasted for: {mins} mins")
		exit("Thanks for playing!")

def scenarioCheck():
	# King Dead
	try:
		boardPieces.index("White_King")
	except:
		win(False)
	
	try:
		boardPieces.index("Black_King")
	except:
		win(True)



		
# --------------- Main program ---------------




board()
time2.stopwatch_start()

while True:

	scenarioCheck()
	checkVar = checkTest(boardPieces)
	if checkVar["Black"]:
		print("Black is in check!")
	elif checkVar["White"]:
		print("White is in check!")

	try:
		xStart = int(input("Enter the x co-ordinate of the piece: "))
		clear()
		board()
		yStart = int(input("Enter the y co-ordinate of the piece: "))
	except:
		print("Please enter numbers!!")
		input("[press enter to continue]")
		clear()
		board()
		continue
	
	clear()
	board()

	try:
		numStart = calculateNum(xStart, yStart)
	except:
		print("That is not a co-ordinate on the board!")
		input("[press enter to try again]")
		clear()
		board()
		continue

	try:
		xEnd = int(input("Entet the x co-ordinate of the end square: "))
		clear()
		board()
		yEnd = int(input("Entet the y co-ordinate of the end square: "))
	except:
		print("Please enter numbers!!")
		input("[press enter to try again]")
		clear()
		board()
		continue
	
	clear()
	board()

	try:
		numEnd = calculateNum(xEnd,yEnd)
	except:
		print("That is not a co-ordinate on the board!")
		input("[press enter to try again]")
		clear()
		board()
		continue

	if valid(numStart, numEnd):
		move(numStart, numEnd)
	else:
		print("Invalid Move!")
		input("[press enter to try again]")
		clear()
		board()
		continue

	lists = allMoves(boardPieces)
	
	computerMove()
	
	clear()
	board()

