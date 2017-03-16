import os
import numpy as np

color_map = {
'w':'white',
'b':'black',
'_': '_'
}

piece_map = {
"" : "blank",
'_': 'blank',
'r': 'rook', 
'q': 'queen',
'p': 'pawn',
'n': 'knight',
'k': 'king',
'b': 'bishop'
}

def fen_to_board(path):
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

def get_picture_name( square_colour, piece_colour, piece_type):
        #given the type of piece it is, returns the name of the picture it correlates to
        return color_map[piece_colour] + '_' + piece_map[piece_type] + '_' + square_colour + ".png"


def position_picture(board, row, col):
    #given a board, returns the information at the specific square
    square_colour = ""
    piece_colour = ""
    piece_type = ""

    if (row + col) % 2 == 1:
        square_colour = "b"
    else:
        square_colour = "w"

    piece_type = board[row][col].lower()
    if piece_type == '_':
    	piece_type = ''

    if board[row][col].isupper():
        piece_colour = "w"
    elif board[row][col].islower():
        piece_colour = "b"
    else:
        piece_colour = "_" 

    return (square_colour, piece_colour, piece_type)