from tkinter import *
from tkinter import ttk

def show_deposit(account_win):
    dep = Toplevel(account_win)
    dep.title("Deposit")
    frm = ttk.Frame(dep, padding=15)
    frm.grid()

    ttk.Label(frm, text="Enter amount:").grid(column=0, row=0)
    ttk.Entry(frm).grid(column=1, row=0)
    ttk.Button(frm, text="Confirm").grid(column=0, row=1, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (dep.destroy(), account_win.deiconify())).grid(column=0, row=2, columnspan=2)

    account_win.withdraw()
