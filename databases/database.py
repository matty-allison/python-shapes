from tkinter import*
from tkinter import messagebox
import mysql.connector
root = Tk()
root.title("Log in")
root.geometry("500x300")
root.config(bg='cyan')
class database:
    def __init__(self, master):
        self.label1 = Label(master, text="Please enter your username:")
        self.label1.place(x=30, y=40)
        self.label1.config(bg="cyan", font=("bold", 11))
        self.label2 = Label(master, text="Please enter your password:")
        self.label2.place(x=30, y=100)
        self.label2.config(bg="cyan", font=("bold", 11))
        self.entry1 = Entry(master)
        self.entry1.place(x=250, y=40)
        self.entry2 = Entry(master)
        self.entry2.place(x=250, y=100)
        self.entry2.config(show="*")
        self.btn1 = Button(master, text="Log in", command=self.login)
        self.btn1.place(x=300, y=170)
        self.btn1.config(bg="lightblue", borderwidth="10")
        self.btn2 = Button(master, text="Register new user", command=self.register)
        self.btn2.place(x=50, y=170)
        self.btn2.config(bg="lightblue", borderwidth="10")

    def register(self):
        try:
            if self.entry1.get() == "" or self.entry2.get() == "":
                messagebox.showerror('STATUS', "please enter a name and password")
            else:
                db = mysql.connector.connect(
                    host='127.0.0.1',
                    user='lifechoices',
                    password='@Lifechoices1234',
                    auth_plugin='mysql_native_password',
                    database='hostpitals'
                    )
                cursor = db.cursor()
                code = "INSERT INTO hospitalusers (user, password) VALUES (%s, %s)"
                values = (self.entry1.get(), self.entry2.get())
                cursor.execute(code, values)

                db.commit()
                messagebox.showinfo('STATUS', "Welcome, you are now registered")
        except ValueError:
            if self.entry1.get() != str:
                messagebox.showerror('STATUS', "Invalid, name can not contain digits")
            if self.entry2.get() != int:
                messagebox.showerror('STATUS', "Invalid, password must be digits")

    def login(self):
         db = mysql.connector.connect(
                    host='127.0.0.1',
                    user='lifechoices',
                    password='@Lifechoices1234',
                    auth_plugin='mysql_native_password',
                    database='hostpitals'
                    )
         my_cursor = db.cursor()
         my_cursor.execute("SELECT * FROM hospitalusers")

         for i in my_cursor:
             if self.entry1.get() == i[0] and self.entry2.get() == i[1]:
                 messagebox.showinfo('STATUS', "Welcome back")
                 break
             if self.entry1.get() != i[0] and self.entry2.get() != i[1]:
                 messagebox.showerror('STATUS', "Invalid, The password or username does not exist or is incorrect")
                 self.entry1.delete(0, END)
                 self.entry2.delete(0, END)

x = database(root)
root.mainloop()
