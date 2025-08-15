from tkinter import *
from tkinter import ttk

def show_transfer(account_win):
    tf = Toplevel(account_win)
    tf.title("Transfer")
    frm = ttk.Frame(tf, padding=15)
    frm.grid()

    ttk.Label(frm, text="Recipient Acc No:").grid(column=0, row=0)
    ttk.Entry(frm).grid(column=1, row=0)
    ttk.Label(frm, text="Enter amount:").grid(column=0, row=1)
    ttk.Entry(frm).grid(column=1, row=1)

    ttk.Button(frm, text="Confirm").grid(column=0, row=2, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (tf.destroy(), account_win.deiconify())).grid(column=0, row=3, columnspan=2)

    account_win.withdraw()
