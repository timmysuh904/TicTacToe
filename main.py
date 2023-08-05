import tkinter
from tkinter import *
import customtkinter
from board import Board
from mediumbot import mediumbot
from player import Player
from easybot import easybot
from hardbot import hardbot

board = Board()
player1 = Player.x
player2 = Player.o
bot = None
status = None


def raise_frame(frames, mode):
    global status
    global bot
    global board
    global buttons
    global winningLabel

    if mode == "Easy":
        status = "AI"
        bot = easybot("O")

    elif mode == "Medium":
        status = "AI"
        bot = mediumbot("O")

    elif mode == "Hard":
        status = "AI"
        bot = hardbot("O")

    elif mode == "co-op":
        status = "co-op"

    elif mode == "Main Menu":
        board = Board()
        bot = None
        status = None
        buttons = create_board()
        winningLabel.configure(text="")

    frames.tkraise()


def handle_click(shape, move, box):
    global board
    global buttons
    global bot
    global status
    gameBoard = board

    if gameBoard.find_winner() is None and len(gameBoard.moves) < 9:
        if gameBoard.is_space_empty(move[0], move[1]):
            if len(gameBoard.moves) in [0, 2, 4, 6, 8] and status == "AI" and len(gameBoard.moves) != 8:
                gameBoard.make_move(move[0], move[1], "X")
                buttons[move[0]][move[1]].configure(background="grey", text="X")
                if gameBoard.find_winner() is None:
                    botmove = bot.select_move(gameBoard)
                    board.make_move(botmove[0], botmove[1], "O")
                    buttons[botmove[0]][botmove[1]].configure(background="grey", text="O")
            elif len(gameBoard.moves) in [1, 3, 5, 7, 9] and status == "co-op":
                gameBoard.make_move(move[0], move[1], "O")
                buttons[move[0]][move[1]].configure(background="grey", text="O")

            elif len(gameBoard.moves) in [0, 2, 4, 6, 8]:
                gameBoard.make_move(move[0], move[1], "X")
                buttons[move[0]][move[1]].configure(background="grey", text="X")

    if len(gameBoard.moves) >= 5:
        if gameBoard.find_winner() == 'X':
            box.configure(text="X is the Winner!")
            box.lift()
        elif gameBoard.find_winner() == 'O':
            box.configure(text="O is the Winner!")
            box.lift()
        elif len(gameBoard.moves) == 9 and gameBoard.find_winner() is None:
            box.configure(text="Tie!")
            box.lift()


def create_board():
    res = []
    for a in range(3):
        temp = []
        for b in range(3):
            button = tkinter.Button(gameFrame, text=".", height=5)
            button.grid(row=a, column=b, sticky="nsew", padx=10, pady=10)
            button.configure(command=lambda row=a, column=b: handle_click(button['text'],
                                                                          [row, column], winningLabel))
            temp.append(button)
        res.append(temp)
    return res


# System Settings
customtkinter.set_appearance_mode("System")

# App
root = tkinter.Tk()
root.geometry("800x600")
root.title("TicTacToe")
# root.resizable(False, False)

# Frame
startingFrame = tkinter.Frame(root)
AIFrame = tkinter.Frame(root)
gameFrame = tkinter.Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
for frame in (startingFrame, AIFrame, gameFrame):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

# UI Elements
title = tkinter.Label(startingFrame, text="Select a Mode!")
title.pack(side=tkinter.TOP, padx=310, pady=25)
oneplayer = Button(startingFrame, text="One Player", command=lambda: raise_frame(AIFrame, "AI"))
oneplayer.pack(side=tkinter.TOP, pady=10)
twoplayer = tkinter.Button(startingFrame, text="Two Player", command=lambda: raise_frame(gameFrame, "co-op"))
twoplayer.pack(side=tkinter.TOP)

# choosing AI difficulty
back = tkinter.Button(AIFrame, text="Back", command=lambda: raise_frame(startingFrame, "start"))
back.pack(side=tkinter.BOTTOM, anchor=SW, padx=10, pady=10)
aimode = tkinter.Label(AIFrame, text="Select a Difficulty!")
aimode.pack(side=tkinter.TOP, padx=310, pady=10)
easy = Button(AIFrame, text="Easy", command=lambda: raise_frame(gameFrame, "Easy"))
easy.pack(side=tkinter.TOP, pady=10)
medium = Button(AIFrame, text="Medium", command=lambda: raise_frame(gameFrame, "Medium"))
medium.pack(side=tkinter.TOP, pady=10)
hard = Button(AIFrame, text="Hard", command=lambda: raise_frame(gameFrame, "Hard"))
hard.pack(side=tkinter.TOP, pady=10)

# gameboard
winningLabel = tkinter.Label(gameFrame, text="", height=15, width=15)
winningLabel.grid(row=3, column=0, columnspan=3, pady=10)
buttons = create_board()
back2 = tkinter.Button(gameFrame, text="Main Menu", command=lambda: raise_frame(startingFrame, "Main Menu"))
back2.grid(row=4, column=0, sticky="w", padx=5, pady=5)

for i in range(3):
    gameFrame.grid_rowconfigure(i, weight=1)
    gameFrame.grid_columnconfigure(i, weight=1)

raise_frame(startingFrame, "start")
# Running
root.mainloop()
