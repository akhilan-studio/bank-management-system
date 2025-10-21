from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m
import account
import random

 
my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')

def Transfer(accno,amt):
    global my
    cu1.cursor()
    

def deposit(acc,bal):
    global my
 
def deposit(acc,bal):
    my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')
 
    cu1=my.cursor()
    ex='update main set balance={new} where accno={acc};'
    new=balance(acc)+int(bal)
    cu1.execute(ex.format(new=new,acc=acc))
    my.commit()
    cu1.close()
 
    cu2=my.cursor()
    if bal[0]=='-':
        cu2.execute('insert into log values({accno},"withdraw",{amount},Null,sysdate())'.format(accno=acc,amount=bal))
    else:
        cu2.execute('insert into log values({accno},"deposit",{amount},Null,sysdate())'.format(accno=acc,amount=bal))
    cu2.close()
    my.commit()
    
def balance(accno):
    global my
 
    my.close()

def balance(accno):
    my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')
 
    cu1=my.cursor()
    ex="select balance from main where accno={accno};"
    cu1.execute(ex.format(accno=accno))
    data=cu1.fetchone()
    cu1.close()
    return data[0]

def loginchecker(passwd,accno,root):
 
    global my
 
 
    root.withdraw()
    if accno.isdigit():
        accno=int(accno)
    else:
        messagebox.showerror('invalid value','enter an account no')
 
 
    my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')
 
    cu1=my.cursor()
    ex="select accno,password from main where accno={accno} and password='{passwd}';"
    cu1.execute(ex.format(accno=accno,passwd=passwd))
    data=cu1.fetchone()
    cu1.close()
    if data:
        account.show_account(root,accno)
    else:
        messagebox.showerror("Login Failed", "Invalid account number or password")
        root.deiconify()

def Accgen(name,DOB,passwd,root):
 
    global my
 
    my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')
 
    cu1=my.cursor()
    while True:
        x=random.randint(100,999)
        ex='select accno from main where accno='+str(x)+';'
        cu1.execute(ex)
        if cu1.fetchall()==[]:
            break
    cu1.close()
    ex="insert into main values({x},'{name}','{DOB}','{passwd}',0);"
    cu2=my.cursor()
    cu2.execute(ex.format(x=x,name=name,DOB=DOB,passwd=passwd))
    my.commit()
    cu2.close()
    cu2=my.cursor()
    cu2.execute('insert into log values({accno},"account created",Null,Null,sysdate())'.format(accno=x))
    my.commit()
    cu2.close()
    x='accountNo:'+str(x)
    ne=Toplevel(root)
    ne.title("New Account")
    frm = ttk.Frame(ne, padding=(90,15,90,15))
    frm.grid()
    ttk.Label(frm, text=x).grid(column=0, row=0)
    ttk.Button(frm, text="main page", command=lambda: (ne.destroy(),root.deiconify())).grid(column=0, row=4, columnspan=2)
