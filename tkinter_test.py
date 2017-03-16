from Tkinter import *
from PIL import Image, ImageTk
import board_utils
import os

SQUARE_SIZE = 65

class Application(Frame):

    chess_engine_name = "upload"

    def say_hi(self):
        print "hi there, everyone!"

    def create_widgets(self):
        self.create_menubar()
        self.create_board()
        self.create_buttons()

    
    def create_menubar(self):

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Upload", menu=menu)
        menu.add_command(label="Engine", command=self.shit)
        menu.add_command(label="PGN Game", command=self.shit)
        menu.add_command(label="Engine", command=self.shit)
        menu.add_command(label="Engine", command=self.shit)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")

        self.master.config(menu=self.menubar)   


    def shit(self):
        print "shit"

    def create_buttons(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

        self.bull = Button(self)
        self.bull["text"] = "bull"
        self.bull.pack(side=BOTTOM)
        self.bull['command'] = self.shit



    def create_piece_pics(self):
        for piece_colour in ('b', 'w'):
            for piece_type in ('b', 'q', 'r', 'k', 'n', 'p'):
                for square_colour in ('b', 'w'):
                    self.piece_pics[square_colour+piece_type+piece_colour] = board_utils.get_picture_name(square_colour, piece_colour, piece_type)

        return



    def create_board(self):
        #creates the chess board is printed to screen
        self.board = Frame(self)

        self.piece_pics = {}

        self.create_piece_pics()


        board_type = board_utils.fen_to_board("init/initial_position.fen")
        self.chess_window = Canvas(self.board, width=SQUARE_SIZE*8, height=SQUARE_SIZE*8, bd=1)
        for i in range(8):
            for j in range(8):
                    square_colour, piece_colour, piece_type = board_utils.position_picture(board_type, i, j)
                    im = Image.open("chess_pieces/png/" + board_utils.get_picture_name(square_colour, piece_colour, piece_type))
                    photo = ImageTk.PhotoImage(im)
                    self.chess_window.create_image((i+.5)*SQUARE_SIZE, (j+.5)*SQUARE_SIZE, image=photo)

        self.chess_window.create_line(4, 4, 4, 8*SQUARE_SIZE)
        self.chess_window.create_line(4, 4, 8*SQUARE_SIZE, 4)
        self.chess_window.create_line(8*SQUARE_SIZE, 4, 8*SQUARE_SIZE, 8*SQUARE_SIZE)
        self.chess_window.create_line(4, 8*SQUARE_SIZE, 8*SQUARE_SIZE, 8*SQUARE_SIZE)
        self.chess_window.pack(side=RIGHT)

        self.board.pack(side=RIGHT)

        return

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()