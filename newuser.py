from tkinter import *
from tkinter import ttk
import random

def Accgen(root):
    x=random.randint(100,999)
    x="account No:"+str(x)
    ne=Toplevel(root)
    ne.title("New Account")
    frm = ttk.Frame(ne, padding=(90,15,90,15))
    frm.grid()

    ttk.Label(frm, text=x).grid(column=0, row=0)
    ttk.Button(frm, text="main page", command=lambda: (ne.destroy(),root.deiconify())).grid(column=0, row=4, columnspan=2)
    
def show_new_user(root):
    nu = Toplevel(root)
    nu.title("New Account")
    frm = ttk.Frame(nu, padding=15)
    frm.grid()

    ttk.Label(frm, text="Name:").grid(column=0, row=0)
    ttk.Entry(frm).grid(column=1, row=0)

    ttk.Label(frm, text="DOB:").grid(column=0, row=1)
    ttk.Entry(frm).grid(column=1, row=1)

    ttk.Label(frm, text="Password:").grid(column=0, row=2)
    ttk.Entry(frm, show="*").grid(column=1, row=2)

    ttk.Button(frm, text="Create", command=lambda: (nu.destroy(),Accgen(root))).grid(column=0, row=3, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (nu.destroy(),root.deiconify())).grid(column=0, row=4, columnspan=2)

    root.withdraw()
