from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql_connection as m


    
def show_new_user(root):
    nu = Toplevel(root)
    nu.title("New Account")
    frm = ttk.Frame(nu, padding=30)
    frm.grid()

    ttk.Label(frm, text="Name:").grid(column=0, row=0)
    name=StringVar()
    ttk.Entry(frm,textvariable=name).grid(column=1, row=0)

    ttk.Label(frm, text="DOB:").grid(column=0, row=1)
    day=StringVar()
    month=StringVar()
    year=StringVar()
    inrfrm=ttk.Frame(frm)
    inrfrm.grid(column=1,row=1)
    ttk.Spinbox(inrfrm,from_=1,to=31,textvariable=day,width=5).grid(column=0,row=0)
    ttk.Spinbox(inrfrm,from_=1,to=12,textvariable=month,width=5).grid(column=1,row=0)
    ttk.Spinbox(inrfrm,from_=1800,to=2025,textvariable=year,width=5).grid(column=2,row=0)
    
    ttk.Label(frm, text="Password:").grid(column=0, row=2)
    passwd=StringVar()
    ttk.Entry(frm, show="*",textvariable=passwd).grid(column=1, row=2)

    ttk.Button(frm, text="Create", command=lambda: checkvalues(nu,name.get(),passwd.get(),root,nu,day.get(),month.get(),year.get())).grid(column=0, row=3, columnspan=2, pady=5)
    ttk.Button(frm, text="Back", command=lambda: (nu.destroy(),root.deiconify())).grid(column=0, row=4, columnspan=2)

    root.withdraw()

def checkvalues(nu,name,passwd,root,new_user,day,month,year):
    if len(month)==1:
        month='0'+month
    if len(day)==1:
        day='0'+day
    DOB=year+'-'+month+'-'+day
    if passwd=='' or name=='' or DOB=='':
        messagebox.showerror('empty value','A requied value is empty')
    else:
        m.Accgen(name,DOB,passwd,root,new_user)