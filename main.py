from tkinter import *
from tkinter import ttk
import account
import newuser

def login():
    root.withdraw()
    account.show_account(root)

def open_new_user():
    root.withdraw()
    newuser.show_new_user(root)

root = Tk()
root.title("Login")
frm = ttk.Frame(root, padding=15)
frm.grid()

ttk.Label(frm, text="Account No:").grid(column=0, row=0)
ttk.Entry(frm).grid(column=1, row=0)

ttk.Label(frm, text="Password:").grid(column=0, row=1)
ttk.Entry(frm, show="*").grid(column=1, row=1)

ttk.Button(frm, text="Login", command=login).grid(column=0, row=2, columnspan=2, pady=5)
ttk.Button(frm, text="Create Account", command=open_new_user).grid(column=0, row=3, columnspan=2, pady=5)

root.mainloop()
