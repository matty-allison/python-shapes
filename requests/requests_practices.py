from tkinter import *
import requests

root = Tk()
root.title("Chuck Norris Jokes")
root.geometry("600x300")
frame = Frame(root)
root.config(bg="red")

response = requests.get("https://api.chucknorris.io/jokes/random")

data = response.json()
print(data['value'])

root.mainloop()
