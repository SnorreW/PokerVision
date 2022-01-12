import tkinter
from tkinter import *
import pokerVision

#GUI for the the program

master = Tk()
myText = StringVar()
myTextEV = StringVar()
myTextPlayers = StringVar()
num_players = tkinter.IntVar()
Label(master, text="AllIn_Loses:").grid(row=0, sticky=W)
Label(master, text="AllIn_Winnings:").grid(row=1, sticky=W)
Label(master, text="Fold_Winnings:").grid(row=2, sticky=W)
Label(master, text="Fold_Percent:").grid(row=3, sticky=W)
Label(master, text="Equity:").grid(row=4, sticky=W)
Label(master, text="Call_Amount:").grid(row=5, sticky=W)
Label(master, text="players:").grid(row=6, sticky=W)
Label(master, text="Result:").grid(row=7, sticky=W)
Label(master, text="EV:").grid(row=8, sticky=W)
result1 = Label(master, text="", textvariable=num_players).grid(row=6, column=1, sticky=W)
result2 = Label(master, text="", textvariable=myText).grid(row=7, column=1, sticky=W)
result3 = Label(master, text="", textvariable=myTextEV).grid(row=8, column=1, sticky=W)


AllIn_Loses = Entry(master)
AllIn_Winnings = Entry(master)
Fold_Winnings = Entry(master)
Fold_Percent = Entry(master)
Equity = Entry(master)
Call_Amount = Entry(master)

AllIn_Loses.grid(row=0, column=1)
AllIn_Winnings.grid(row=1, column=1)
Fold_Winnings.grid(row=2, column=1)
Fold_Percent.grid(row=3, column=1)
Equity.grid(row=4, column=1)
Call_Amount.grid(row=5, column=1)

b = Button(master, text="Calculate", command=lambda: pokerVision.scan_screen(num_players.get()))
b.grid(row=0, column=2, columnspan=2, rowspan=6, sticky=W+E+N+S, padx=5, pady=5)


def increase():
    num_players.set(num_players.get() + 1)
def decrease():
    num_players.set(num_players.get() - 1)

plus = Button(master, text="+", command=increase)
plus.grid(row=6, column=3, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)
minus = Button(master, text="-", command=decrease)
minus.grid(row=6, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)

mainloop()
