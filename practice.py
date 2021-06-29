from tkinter import *
root = Tk()
root.geometry("400x400")
root.config(bg="blue")

button = Button(root, text="Click me")
button.place(x=160, y=150)
button.config(bg="black", fg="white", borderwidth="10")

root.mainloop()
