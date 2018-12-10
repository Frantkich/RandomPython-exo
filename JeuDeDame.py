import os 
import random

BOARD = [
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,1,0,1,0,1,0,1,0],
		[0,1,0,1,0,1,0,1,0,1,0,0],
		[0,0,1,0,1,0,1,0,1,0,1,0],
		[0,1,0,'pawn_black',0,1,0,'pawn_black',0,1,0,0],
		[0,0,1,0,1,0,1,0,1,0,1,0],
		[0,1,0,1,0,'queen_white',0,1,0,1,0,0],
		[0,0,1,0,1,0,1,0,1,0,1,0],
		[0,1,0,'pawn_black',0,1,0,'pawn_black',0,1,0,0],
		[0,0,1,0,1,0,1,0,1,0,1,0],
		[0,1,0,1,0,1,0,1,0,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		]

ALPHABET = ["A","B","C","D","E","F","G","H","I","J"]
NUMBER = ["0","1","2","3","4","5","6","7","8","9"]

score_white = 0
score_black = 0

def ResetBoard(player):
	for y in range(1,11):
		for x in range(1,11):
			if player == 'white':
				if BOARD[y][x] == 'av_pawn_white' or BOARD[y][x] == 'sel_pawn_white' or BOARD[y][x] == 'tar_pawn_white':
					BOARD[y][x] = 'pawn_white'

				if BOARD[y][x] == 'av_queen_white' or BOARD[y][x] == 'sel_queen_white' or BOARD[y][x] == 'tar_queen_white':
					BOARD[y][x] = 'queen_white'

			if player == 'black': 
				if BOARD[y][x] == 'av_pawn_black' or BOARD[y][x] == 'sel_pawn_black' or BOARD[y][x] == 'tar_pawn_black':
					BOARD[y][x] = 'pawn_black'

				if BOARD[y][x] == 'av_queen_black' or BOARD[y][x] == 'sel_queen_black' or BOARD[y][x] == 'tar_queen_black':
					BOARD[y][x] = 'queen_black'

def DispBoard():
	os.system("cls")
	print(" ", end='')
	for n in range(10):
		print("", ALPHABET[n], end='')
	print()

	print(" ╔", end='')
	for loop in range(10):
		print("══", end='')
	print("╗")

	for y in range(1, 11):
		print(y-1, end='')
		print("║", end='')
		for x in range(1, 11):
			if BOARD[y][x] == 0:
				print("██", end='')
			if BOARD[y][x] == 1:
				print("  ", end='')

			if BOARD[y][x] == 'pawn_white':
				print("○○", end='')
			if BOARD[y][x] == 'tar_pawn_white':
				print('\x1b[6;31;40m'+'○○'+'\x1b[0m', end='')
			if BOARD[y][x] == 'av_pawn_white':
				print('\x1b[6;32;40m'+'○○'+'\x1b[0m', end='')
			if BOARD[y][x] == 'sel_pawn_white':
				print('\x1b[6;34;40m'+'○○'+'\x1b[0m', end='')

			if BOARD[y][x] == 'queen_white':
				print("●●", end='')
			if BOARD[y][x] == 'tar_queen_white':
				print('\x1b[6;31;40m'+'●●'+'\x1b[0m', end='')
			if BOARD[y][x] == 'av_queen_white':
				print('\x1b[6;32;40m'+'●●'+'\x1b[0m', end='')
			if BOARD[y][x] == 'sel_queen_white':
				print('\x1b[6;34;40m'+'●●'+'\x1b[0m', end='')

			if BOARD[y][x] == 'pawn_black':
				print("ΔΔ", end='')
			if BOARD[y][x] == 'tar_pawn_black':
				print('\x1b[6;31;40m'+'ΔΔ'+'\x1b[0m', end='')
			if BOARD[y][x] == 'av_pawn_black':
				print('\x1b[6;32;40m'+'ΔΔ'+'\x1b[0m', end='')
			if BOARD[y][x] == 'sel_pawn_black':
				print('\x1b[6;34;40m'+'ΔΔ'+'\x1b[0m', end='')

			if BOARD[y][x] == 'queen_black':
				print("▲▲", end='')
			if BOARD[y][x] == 'tar_queen_black':
				print('\x1b[6;31;40m'+'▲▲'+'\x1b[0m', end='')
			if BOARD[y][x] == 'av_queen_black':
				print('\x1b[6;32;40m'+'▲▲'+'\x1b[0m', end='')
			if BOARD[y][x] == 'sel_queen_black':
				print('\x1b[6;34;40m'+'▲▲'+'\x1b[0m', end='')

		print("║", y-1)
	
	print(" ╚", end='')
	for loop in range(10):
		print("══", end='')
	print("╝")
	print(" ", end='')
	for n in range(10):
		print("", ALPHABET[n], end='')
	print("\n")

def RandomRepartiton(nb_pawn):
	while nb_pawn != 0:
		x = random.randint(1, 11)
		y = random.randint(1, 11)
		if BOARD[y][x] == 1:
			nb_pawn -= 1
			BOARD[y][x] = 'pawn_white'
		x = random.randint(1, 11)
		y = random.randint(1, 11)
		if BOARD[y][x] == 1:
			nb_pawn -= 1
			BOARD[y][x] = 'pawn_black'

def AvailablePawn(player):
	for y in range(1, 11):
		for x in range(1, 11):
			if player == 'white':
				if BOARD[y][x] == 'pawn_white':
					if BOARD[y -1][x +1] == 1 or BOARD[y -1][x -1] == 1 or ( 'black' in str(BOARD[y -1][x +1]) and  BOARD[y -2][x +2] == 1 ) or ( 'black' in str(BOARD[y -1][x -1]) and BOARD[y -2][x -2] == 1 ):
						BOARD[y][x] = 'av_pawn_white'

				if BOARD[y][x] == 'queen_white':
					if BOARD[y -1][x +1] == 1 or BOARD[y -1][x -1] == 1 or BOARD[y +1][x +1] == 1 or BOARD[y +1][x -1] == 1 or ( 'black' in str(BOARD[y -1][x +1]) and  BOARD[y -2][x +2] == 1 ) or ( 'black' in str(BOARD[y -1][x -1]) and BOARD[y -2][x -2] == 1 ) or ( 'black' in str(BOARD[y +1][x +1]) and BOARD[y +2][x +2] == 1 ) or ( 'black' in str(BOARD[y +1][x -1]) and BOARD[y +2][x -2] == 1 ):
						BOARD[y][x] = 'av_queen_white'

			if player == 'black':
				if BOARD[y][x] == 'pawn_black':
					if BOARD[y +1][x +1] == 1 or BOARD[y +1][x -1] == 1 or ( 'white' in str(BOARD[y +1][x +1]) and BOARD[y +2][x +2] == 1 ) or ( 'white' in str(BOARD[y +1][x -1]) and BOARD[y +2][x -2] == 1 ):
						BOARD[y][x] = 'av_pawn_black'

				if BOARD[y][x] == 'queen_black':
					if BOARD[y -1][x +1] == 1 or BOARD[y -1][x -1] == 1 or BOARD[y +1][x +1] == 1 or BOARD[y +1][x -1] == 1 or ( 'black' in str(BOARD[y -1][x +1]) and  BOARD[y -2][x +2] == 1 ) or ( 'black' in str(BOARD[y -1][x -1]) and BOARD[y -2][x -2] == 1 ) or ( 'black' in str(BOARD[y +1][x +1]) and BOARD[y +2][x +2] == 1 ) or ( 'black' in str(BOARD[y +1][x -1]) and BOARD[y +2][x -2] == 1 ):
						BOARD[y][x] = 'av_queen_black'

def DispScore(player):
	global score_white
	global score_black
	os.system("cls")
	print("\nIt's the turn of", player,"\n\nScore of White :", score_white,"\nScore of Black :", score_black)
	input()

def Selected(player):
	selected_input = input("Which pawn do you want to move ? > ")
	while True:
		if selected_input == 'quit':
			break
		if len(selected_input) == 2:
			if selected_input[0] in ALPHABET and selected_input[1] in NUMBER:
				X_initial = ALPHABET.index(selected_input[0]) +1
				Y_initial = int(selected_input[1]) +1

				if player == 'white':
					if BOARD[Y_initial][X_initial] == 'av_pawn_white':
						BOARD[Y_initial][X_initial] = 'sel_pawn_white'
						break
					if BOARD[Y_initial][X_initial] == 'av_queen_white':
						BOARD[Y_initial][X_initial] = 'sel_queen_white'
						break

				elif player == 'black':
					if BOARD[Y_initial][X_initial] == 'av_pawn_black':
						BOARD[Y_initial][X_initial] = 'sel_pawn_black'
						break
					if BOARD[Y_initial][X_initial] == 'av_queen_black':
						BOARD[Y_initial][X_initial] = 'sel_queen_black'
						break
				else:
					DispBoard()
					print("You have to pick a green pawn.")
			else:
				DispBoard()
				print("You have to pick a letter between A and J\nadd to a digit between 0 and 9.")
		else:
			DispBoard()
			print("Pick a letter and a digit.")
		print("Try again > ", end='')
		selected_input = input()

	if selected_input == 'quit':
		return 1
	else:
		DispBoard()
		print("Valid pawn.")
		QueenPoss(player, Y_initial, X_initial)
		Direction(player,Y_initial,X_initial)

def Direction(player, Y_initial, X_initial):
	dir_input = input("Where to pose your pawn ? > ")
	while True:
		if dir_input == 'cancel':
			ResetBoard(player)
			os.system("cls")
			AvailablePawn(player)
			DispBoard()
			Selected(player)
			break
		if len(dir_input) == 2:
			if dir_input[0] in ALPHABET and dir_input[1] in NUMBER:
				X_final = ALPHABET.index(dir_input[0]) +1	
				Y_final = int(dir_input[1]) +1
				if BOARD[Y_final][X_final] == 1:
					if Action(player, Y_initial, X_initial, Y_final, X_final) == 1:
						break
				else:
					DispBoard()
					print("You have to pose your pawn on an empty case.")
			else:
				DispBoard()
				print("You have to pick a letter between A and J\nadd to a digit between 0 and 9.")
		else:
			DispBoard()
			print("Pick a letter and a digit.")
		print("Try again > ", end='')
		dir_input = input()

def Move(player, Y_initial, X_initial, Y_final, X_final):
	if BOARD[Y_initial][X_initial] == 'sel_pawn_white' or BOARD[Y_initial][X_initial] == 'sel_pawn_black':
		if X_final == (X_initial +1) or X_final == (X_initial -1):
			if player == 'white':
				BOARD[Y_final][X_final] = 'pawn_white'
			if player == 'black':
				BOARD[Y_final][X_final] = 'pawn_black'
			BOARD[Y_initial][X_initial] = 1
			print("Pawn moved")
			input()
			return
	if BOARD[Y_initial][X_initial] == 'sel_queen_white' or BOARD[Y_initial][X_initial] == 'sel_queen_black':
			if player == 'white':
				BOARD[Y_final][X_final] = 'queen_white'
			if player == 'black':
				BOARD[Y_final][X_final] = 'queen_black'
			BOARD[Y_initial][X_initial] = 1
			print("Pawn moved")
			input()
			return
			
def Game(player):
	DispScore(player)
	TransPawn()
	AvailablePawn(player)
	DispBoard()
	if Selected(player) == 1:
		if player == 'white':
			os.system("cls")
			print("\n\nThe player White surrender...\n\nThe player Black win the game !")
			input()
			return 1
		elif player == 'black':
			os.system("cls")
			print("\n\nThe player Black surrender...\n\nThe player White win the game !")
			input()
			return 1
	ResetBoard(player)
	return 0

def Eat(player, Y_initial, X_initial, Y_final, X_final):
	global score_white
	global score_black

	if player == 'white':
		score_white += 1
		if BOARD[Y_initial][X_initial] == 'sel_pawn_white':
			BOARD[Y_final][X_final] = 'pawn_white'
		if BOARD[Y_initial][X_initial] == 'sel_queen_white':
			BOARD[Y_final][X_final] = 'queen_white'
	if player == 'black':
		score_black +=1
		if BOARD[Y_initial][X_initial] == 'sel_pawn_black':
			BOARD[Y_final][X_final] = 'pawn_black'
		if BOARD[Y_initial][X_initial] == 'sel_queen_black':
			BOARD[Y_final][X_final] = 'queen_black'

	BOARD[Y_initial][X_initial] = 1

def QueenDplcmt(player, Y_initial, X_initial, Y_final, X_final):
	cond = 0
	cond = 0
	Xpos = 0
	Ypos = 0
	for xy in range(1, abs(Y_final -Y_initial) +1):
		if (Y_final -Y_initial) > 0 and (X_final -X_initial) > 0:
			if player == 'white' and BOARD[Y_initial +xy][X_initial +xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial +xy][X_initial +xy] == 'pawn_white':
				if cond == 1:
					cond = 2
				if cond == 0:
					cond = 1
					Ypos = Y_initial +xy
					Xpos = X_initial +xy

		if (Y_final -Y_initial) < 0 and (X_final -X_initial) > 0:
			if player == 'white' and BOARD[Y_initial -xy][X_initial +xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial -xy][X_initial +xy] == 'pawn_white':
				if cond == 1:
					cond = 2
				if cond == 0:
					cond = 1
					Ypos = Y_initial -xy
					Xpos = X_initial +xy

		if (Y_final -Y_initial) > 0 and (X_final -X_initial) < 0:
			if player == 'white' and BOARD[Y_initial +xy][X_initial -xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial +xy][X_initial -xy] == 'pawn_white':
				if cond == 1:
					cond = 2
				if cond == 0:
					cond = 1
					Ypos = Y_initial +xy
					Xpos = X_initial -xy

		if (Y_final -Y_initial) < 0 and (X_final -X_initial) < 0:
			if player == 'white' and BOARD[Y_initial -xy][X_initial -xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial -xy][X_initial -xy] == 'pawn_white':
				if cond == 1:
					cond = 2
				if cond == 0:
					cond = 1
					Ypos = Y_initial -xy
					Xpos = X_initial -xy

	if cond == 1:
		print("Pawn", ALPHABET[Xpos -1] +NUMBER[Ypos -1],"eated")
		input()
		Eat(player, Y_initial, X_initial, Y_final, X_final)
		BOARD[Ypos][Xpos] = 1
		QueenPoss(player, Y_final, X_final)
		return 1
	if cond == 0:
		Move(player, Y_initial, X_initial, Y_final, X_final)
		return 1

def QueenPoss(player, Y_initial, X_initial):
	cond = 0
	poss = []
	for xy in range(1, 9):
		if BOARD[Y_initial +xy][X_initial +xy] == 0:
			break
		if player == 'white' and BOARD[Y_initial +xy][X_initial +xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial +xy][X_initial +xy] == 'pawn_white':
			if cond == 1:
				cond = 2
			if cond == 0:
				cond = 1
		if cond == 1:
			poss.append(Y_initial +xy)
			poss.append(X_initial +xy)
			cond = 0
	for xy in range(1, 9):
		if BOARD[Y_initial -xy][X_initial +xy] == 0:
			break
		if player == 'white' and BOARD[Y_initial -xy][X_initial +xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial -xy][X_initial +xy] == 'pawn_white':
			if cond == 1:
				cond = 2
			if cond == 0:
				cond = 1
		if cond == 1:
			poss.append(Y_initial -xy)
			poss.append(X_initial +xy)
			cond = 0

	for xy in range(1, 9):
		if BOARD[Y_initial +xy][X_initial -xy] == 0:
			break
		if player == 'white' and BOARD[Y_initial +xy][X_initial -xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial +xy][X_initial -xy] == 'pawn_white':
			if cond == 1:
				cond = 2
			if cond == 0:
				cond = 1
		if cond == 1:
			poss.append(Y_initial +xy)
			poss.append(X_initial -xy)
			cond = 0

	for xy in range(1, 9):
		if BOARD[Y_initial -xy][X_initial -xy] == 0:
			break
		if player == 'white' and BOARD[Y_initial -xy][X_initial -xy] == 'pawn_black' or player == 'black' and BOARD[Y_initial -xy][X_initial -xy] == 'pawn_white':
			if cond == 1:
				cond = 2
			if cond == 0:
				cond = 1
		if cond == 1:
			poss.append(Y_initial -xy)
			poss.append(X_initial -xy)
			cond = 0
	print(poss)
	input()

def Action(player, Y_initial, X_initial, Y_final, X_final):
	if player == 'white':
		if BOARD[Y_initial][X_initial] == 'sel_pawn_white' and Y_final == (Y_initial -1):
			Move(player, Y_initial, X_initial, Y_final, X_final)
			return 1

		if BOARD[Y_initial][X_initial] == 'sel_pawn_white' and Y_final == (Y_initial -2):
			if BOARD[Y_initial -1][X_initial -1] == 'pawn_black' and X_final == X_initial -2:
				Eat(player, Y_initial, X_initial, Y_final, X_final)
				print("Pawn",ALPHABET[X_initial -2] +NUMBER[Y_initial -2],"eated")
				input()
				BOARD[Y_initial -1][X_initial -1] = 1
				Possible(player, Y_final, X_final)
				return 1

			if BOARD[Y_initial -1][X_initial +1] == 'pawn_black' and X_final == X_initial +2:
				Eat(player, Y_initial, X_initial, Y_final, X_final)
				print("Pawn", ALPHABET[X_initial] +NUMBER[Y_initial -2],"eated")
				input()
				BOARD[Y_initial -1][X_initial +1] = 1
				Possible(player, Y_final, X_final)
				return 1
		if BOARD[Y_initial][X_initial] == 'sel_queen_white' and abs(Y_final -Y_initial) == abs(X_final -X_initial):
			if QueenDplcmt(player, Y_initial, X_initial, Y_final, X_final) == 1:
				return 1

	if player == 'black':
		if BOARD[Y_initial][X_initial] == 'sel_pawn_black' and Y_final == (Y_initial +1):
			Move(player, Y_initial, X_initial, Y_final, X_final)
			return 1

		if Y_final == (Y_initial +2):
			if BOARD[Y_initial +1][X_initial -1] == 'pawn_white' and X_final == X_initial -2:
				Eat(player, Y_initial, X_initial, Y_final, X_final)
				print("Pawn", ALPHABET[X_initial -2]+NUMBER[Y_initial],"eated")
				input()
				BOARD[Y_initial +1][X_initial -1] = 1
				Possible(player, Y_final, X_final)
				return 1

			if BOARD[Y_initial +1][X_initial +1] == 'pawn_white' and X_final == X_initial +2:
				Eat(player, Y_initial, X_initial, Y_final, X_final)
				print("Pawn", ALPHABET[X_initial]+NUMBER[Y_initial],"eated")
				input()
				BOARD[Y_initial +1][X_initial +1] = 1
				Possible(player,Y_final,X_final)
				return 1

		if BOARD[Y_initial][X_initial] == 'sel_queen_black' and abs(Y_final -Y_initial) == abs(X_final -X_initial):
			if QueenDplcmt(player, Y_initial, X_initial, Y_final, X_final) == 1:
				return 1

	else:
		DispBoard()
		print("You can't pose your pawn here.")
		return

def Possible(player, Y_initial, X_initial):
	if player == 'white':
		if BOARD[Y_initial -1][X_initial -1] == 'pawn_black' and BOARD[Y_initial -2][X_initial -2] == 1:
			if BOARD[Y_initial -1][X_initial +1] == 'pawn_black' and BOARD[Y_initial -2][X_initial +2] == 1:
				DispBoard()
				Direction(player, Y_initial, X_initial)
				return
			BOARD[Y_initial][X_initial] = 'sel_pawn_white'
			DispBoard()
			Action(player, Y_initial, X_initial, Y_initial -2, X_initial -2)
			return
		if BOARD[Y_initial -1][X_initial +1] == 'pawn_black' and BOARD[Y_initial -2][X_initial +2] == 1:
			BOARD[Y_initial][X_initial] = 'sel_pawn_white'
			DispBoard()
			input()
			Action(player, Y_initial, X_initial, Y_initial -2, X_initial +2)
			return

	if player == 'black':
		if BOARD[Y_initial +1][X_initial -1] == 'pawn_white' and BOARD[Y_initial +2][X_initial -2] == 1:
			if BOARD[Y_initial +1][X_initial +1] == 'pawn_white' and BOARD[Y_initial +2][X_initial +2] == 1:
				DispBoard()
				Direction(player, Y_initial, X_initial)
				return
			BOARD[Y_initial][X_initial] = 'sel_pawn_black'
			DispBoard()
			Action(player, Y_initial, X_initial, Y_initial +2, X_initial -2)
			return
		if BOARD[Y_initial +1][X_initial +1] == 'pawn_white' and BOARD[Y_initial +2][X_initial +2] == 1:
			BOARD[Y_initial][X_initial] = 'sel_pawn_black'
			DispBoard()
			Action(player, Y_initial, X_initial, Y_initial +2, X_initial +2)
			return
	return

def TransPawn():
	for x in range(1, 11):
		if BOARD[1][x] == 'pawn_white':
			BOARD[1][x] = 'queen_white'
		if BOARD[10][x] == 'pawn_black':
			BOARD[10][x] = 'queen_black'

def main():
	#RandomRepartiton(20)
	while True:
		if Game('white') != 0:
			break
		if Game('black') != 0:
			break
	os.system("cls")
	print("\n\n\n\nThank for playing")
	input()
main()