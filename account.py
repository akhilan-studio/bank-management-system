from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql_connection as m

def show_account(root,accno):
    acc = Toplevel(root)
    acc.title("Account Page")
    frm = ttk.Frame(acc,  padding=(90,15,90,15))
    frm.grid()
    
    
    x=m.balance(accno)
    
    ttk.Label(frm,text=str(x)).grid(column=0, row=0)
    
    ttk.Button(frm, text="Deposit", command=lambda: (acc.destroy(),show_deposit(acc,accno,root))).grid(column=0, row=1)
    ttk.Button(frm, text="Withdraw", command=lambda: (acc.destroy(),show_withdraw(root,accno))).grid(column=1, row=1)
    ttk.Button(frm, text="Transfer", command=lambda: (acc.destroy(),show_transfer(root,accno))).grid(column=0, row=2, columnspan=2)
    ttk.Button(frm, text="Logout", command=lambda: logout(acc, root)).grid(column=0, row=3, columnspan=2, pady=10)
    

def logout(account_win, root):
    account_win.destroy()
    root.deiconify()



def show_deposit(account_win,acc,root):
    dep = Tk()
    dep.title("Deposit")
    frm = ttk.Frame(dep, padding=15)
    frm.grid()
    bal=StringVar(dep)
    ttk.Label(frm, text="Enter amount:").grid(column=0, row=0)
    ttk.Entry(frm,textvariable=bal).grid(column=1, row=0)
    ttk.Button(frm, text="Confirm",command=lambda: (dep.destroy(),depocheck(acc,bal.get()),show_account(root,acc))).grid(column=0, row=1, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (dep.destroy(),show_account(root,acc))).grid(column=0, row=2, columnspan=2)

def depocheck(acc,bal):
    if bal.isdigit():
        if int(bal)<0:
            messagebox.showerror('Invalid ammount','entered amount cannot be negative')
        else:
            m.edit_balance(acc,bal)
    else:
        messagebox.showerror('Invalid ammount','entered amount should number')


def show_transfer(root,accno):
    tf = Tk()
    tf.title("Transfer")
    frm = ttk.Frame(tf, padding=15)
    frm.grid()

    ttk.Label(frm, text="Recipient Acc No:").grid(column=0, row=0)
    accnoto=StringVar(tf)
    ttk.Entry(frm,textvariable=accnoto).grid(column=1, row=0)
    ttk.Label(frm, text="Enter amount:").grid(column=0, row=1)
    amt=StringVar(tf)
    ttk.Entry(frm,textvariable=amt).grid(column=1, row=1)

    ttk.Button(frm, text="Confirm",command=lambda: (tf.destroy(),transfer_check(accno,accnoto.get(),amt.get()),show_account(root, accno))).grid(column=0, row=2, columnspan=2, pady=5)
    ttk.Button(frm, text="Back",command=lambda: (tf.destroy(), show_account(root,accno))).grid(column=0, row=3, columnspan=2)

def transfer_check(accnofr,accnoto,amt):
    if amt.isdigit():
        amt=int(amt)
        if m.balance(accnofr)<amt:
            messagebox.showerror('Invalid amount','you do not have enough balance')
        elif amt<0:
            messagebox.showerror('Invalid ammount','entered amount cannot be negative')
        elif m.balance(accnoto)==None:
            messagebox.showerror('Invalid account','account does not exist')
        else:
            m.Transfer(accnofr,accnoto,amt)
    
    else:
        messagebox.showerror('invalid value','pls enter a number')
def show_withdraw(root,acc):
    wd = Tk()
    wd.title("Withdraw")
    frm = ttk.Frame(wd, padding=15)
    frm.grid()
    bal=StringVar(wd)
    ttk.Label(frm, text="Enter amount:").grid(column=0, row=0)
    ttk.Entry(frm,textvariable=bal).grid(column=1, row=0)
    ttk.Button(frm, text="Confirm",command=lambda: (wd.destroy(),withcheck(acc,bal.get()),show_account(root,acc))).grid(column=0, row=1, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (wd.destroy(),show_account(root,acc))).grid(column=0, row=2, columnspan=2)

def withcheck(acc,bal):
    if bal.isdigit()==False:
        messagebox.showerror('invalid value','pls enter a number')
    elif int(bal)<0:
        messagebox.showerror('Invalid ammount','entered amount cannot be negative')
    elif m.balance(acc)<int(bal):
        messagebox.showerror('Invalid amount','you do not have enough balance')
    else:
        m.edit_balance(acc,'-'+bal)
   