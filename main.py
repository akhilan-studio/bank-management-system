from tkinter import *
from tkinter import ttk
import newuser
import mysql_connection as m
def open_new_user():
    root.withdraw()
    newuser.show_new_user(root)

root = Tk()
root.title("Login")
frm = ttk.Frame(root, padding=15)
frm.grid()

ttk.Label(frm, text="Account No:").grid(column=0, row=0)
accno=StringVar(root)
ttk.Entry(frm,textvariable=accno).grid(column=1, row=0)

ttk.Label(frm, text="Password:").grid(column=0, row=1)
passwd=StringVar(root)
ttk.Entry(frm, show="*",textvariable=passwd).grid(column=1, row=1)

ttk.Button(frm, text="Login", command=lambda: (m.loginchecker(passwd.get(),accno.get(),root),passwd.set(''),accno.set(''))).grid(column=0, row=2, columnspan=2, pady=5)
ttk.Button(frm, text="Create Account", command=open_new_user).grid(column=0, row=3, columnspan=2, pady=5)

root.mainloop()

