## gametracker editor
from tkinter import *
import psutil




Listofgames = []


## read json file from data/folder 

def createAddGameWindow():
    new_window = Toplevel()
    gamenamelable = Label(new_window,text="enter game name",font=('Arial',20,'bold'))
    entryofgamename = Entry(new_window)
    entryofgamename.config(font=('Terminal',20))
    entryofgamename.config(bg='#111111')
    entryofgamename.config(fg='white')

    gametimelable = Label(new_window,text="enter game time",font=('Arial',20,'bold'))
    entryofgametime = Entry(new_window)
    entryofgametime.config(font=('Terminal',20))
    entryofgametime.config(bg='#111111')
    entryofgametime.config(fg='white')

    gamenamelable.grid(row=0,column=0)
    entryofgamename.grid(row=0,column=1)

    gametimelable.grid(row=1,column=0)
    entryofgametime.grid(row=1,column=1)



    def submitgame():
        global Listofgames
        gamename = entryofgamename.get()
        gametime = entryofgametime.get()
        
        gameentry = dict(name=gamename,timeplayed=gametime)

        labname = Label(window,textvariable=f'{gameentry.get('name')}',width=15,height=10)
        labtime = Label(window,textvariable=f'{gameentry.get('timeplayed')}',width=15,height=10)
        labname.pack()
        labtime.pack()
        print(gameentry)
        newlistofgames = Listofgames.append(gameentry)
        Listofgames = newlistofgames
        window.update()
        new_window.destroy()

    submit = Button(new_window,text='submit',command=submitgame)
    submit.grid(row=2)

window = Tk(screenName="Widndow")

addgame = Button(window,text='Add Game',command=createAddGameWindow)
addgame.pack()

window.mainloop()