from Tkinter import *
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

    def create_board(self):
        self.chess_window = Canvas(self, width=SQUARE_SIZE*8, height=SQUARE_SIZE*8, bd=1)
        for i in range(8):
            for j in range(8):
                if (i + j)% 2 == 1:
                    self.chess_window.create_rectangle(i*SQUARE_SIZE ,
                    j*SQUARE_SIZE , i*SQUARE_SIZE + SQUARE_SIZE,
                    j*SQUARE_SIZE + SQUARE_SIZE, fill="cornflower blue",
                    outline="cornflower blue")
                self.chess_window.create_text((i+.5)*SQUARE_SIZE, (j+.5)*SQUARE_SIZE, text=chr(ord('a') + i) + chr(ord('8') - j))
        self.chess_window.create_line(4, 4, 4, 8*SQUARE_SIZE)
        self.chess_window.create_line(4, 4, 8*SQUARE_SIZE, 4)
        self.chess_window.create_line(8*SQUARE_SIZE, 4, 8*SQUARE_SIZE, 8*SQUARE_SIZE)
        self.chess_window.create_line(4, 8*SQUARE_SIZE, 8*SQUARE_SIZE, 8*SQUARE_SIZE)
        self.chess_window.pack(side=RIGHT)
        return

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()