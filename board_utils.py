import os
import numpy as np

def fen_to_board(path):
	print "hi"
	with open(path, "r") as f:

		board = np.chararray((8, 8))

		piece_placement, active_color, castling, en_passant, halfmove, fullmove = f.read().split(' ')
		piece_array = piece_placement.split('/')
		for i in range(len(piece_array)):
			line = piece_array[i]
			j = 0
			for char in line:
				if char.isdigit():
					amount = int(char)
					for l in range(amount):
						board[i][j] = '_'
						j+=1
				else:
					board[i][j] = char
					j+=1
		return board

#def board_to_fen(array)