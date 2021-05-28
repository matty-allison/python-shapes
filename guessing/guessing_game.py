from tkinter import*
import random

window = Tk()
window.title("Guessing Game")
window.geometry("300x300")
window.config(bg="#8cdccd")
frame = Frame(window)

label = Label(window, text="Guess the number")
label.place(x=75, y=20)
label.config(bg="#8cdccd", font=("15"))

enter = Entry(window, width="10")
enter.place(x=100, y=90)
enter.config(font="10")

def game():
    while enter.get() <=100 and enter.get() >=1:
        randnum = random.randint(1, 100)
        count = 1
        count += 1
        if enter.get() > randnum:
            label1.config(text="You guessed to high!")
        elif enter.get() < randnum:
            label1.config(text="You guessed to low!")
        else:
            label1.config(text="Well done you guess right")



btn = Button(window, text="Guess", command=game)
btn.place(x=110, y=140)
btn.config(bg="#5ba798", borderwidth="5", font=("15"))

label1 = Label(window, width="10")
label1.place(x=100, y=200)
label1.config(bg="#5ba798", font=("15"))

window.mainloop()
