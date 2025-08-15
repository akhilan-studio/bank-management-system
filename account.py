from tkinter import *
from tkinter import ttk
import deposit
import withdraw
import transfer

def show_account(root):
    acc = Toplevel(root)
    acc.title("Account Page")
    frm = ttk.Frame(acc,  padding=(90,15,90,15))
    frm.grid()

    ttk.Label(frm, text="Balance: ₹0").grid(column=0, row=0, columnspan=2, pady=5)
    ttk.Button(frm, text="Deposit", command=lambda: deposit.show_deposit(acc)).grid(column=0, row=1)
    ttk.Button(frm, text="Withdraw", command=lambda: withdraw.show_withdraw(acc)).grid(column=1, row=1)
    ttk.Button(frm, text="Transfer", command=lambda: transfer.show_transfer(acc)).grid(column=0, row=2, columnspan=2)
    ttk.Button(frm, text="Logout", command=lambda: logout(acc, root)).grid(column=0, row=3, columnspan=2, pady=10)

def logout(account_win, root):
    account_win.destroy()
    root.deiconify()
