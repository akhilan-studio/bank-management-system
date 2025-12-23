from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as m
import account
import random
 
my=m.connect(host='localhost',user='root',passwd='bloodgod@609',database='bank')

def Transfer(accnofr,accnoto,amt):
    global my
    success=False
    if amt.isdigit()==False:
        messagebox.showerror('Invalid amount','value is wrong')
    elif balance(accnofr)<int(amt):
        messagebox.showerror('Invalid amount','you do not have enough balance')
    elif int(amt)<0:
        messagebox.showerror('Invalid amount','entered amount cannot be negative')
    elif balance(accnoto)==None:
        messagebox.showerror('Invalid account','account does not exist')
    elif accnoto==accnofr:
        messagebox.showerror('invalid input',"can't transfer to self")
    else:
        amt=int(amt)
        cu1=my.cursor()
        amtfr=balance(accnofr)-amt
        amtto=balance(accnoto)+amt
        ex='update main set balance=%s where accno=%s;'
        cu1.execute(ex,(amtfr,accnofr))
        cu1.execute(ex,(amtto,accnoto))
        ex='insert into log values(%s,"Transfer",%s,%s,sysdate())'
        cu1.execute(ex,(accnofr,amt,accnoto))
        my.commit()
        cu1.close()
        success=True
    return success
        
    
def edit_balance(acc,bal):
    global my
    cu1=my.cursor()
    ex='update main set balance=%s where accno=%s;'
    new=balance(acc)+int(bal)
    cu1.execute(ex,(new,acc))
    if bal[0]=='-':
        cu1.execute('insert into log values(%s,"withdraw",%s,Null,sysdate())',(acc,bal))
    else:
        cu1.execute('insert into log values(%s,"deposit",%s,Null,sysdate())',(acc,bal))
    my.commit()
    cu1.close()

def balance(accno):
    global my
    cu1=my.cursor()
    ex="select balance from main where accno=%s;"
    cu1.execute(ex,(accno,))
    data=cu1.fetchone()
    cu1.close()
    if data!=None:
        data=data[0]
    return data

def loginchecker(passwd,accno,root):
    global my
    if not accno.isdigit():
        messagebox.showerror('Invalid value', 'Enter a valid account number')
        return

    accno = int(accno)
    cu1 = my.cursor()
    try:
        cu1.execute("SELECT accno FROM main WHERE accno=%s AND password=%s", (accno, passwd))
        result = cu1.fetchone()
    finally:
        cu1.close()

    if result:
        root.withdraw()
        account.show_account(root, accno)
    else:
        messagebox.showerror("Login Failed", "Invalid account number or password")

def Accgen(name,DOB,passwd,root,nu):
    global my
    cu1=my.cursor()
    while True:
        accno=random.randint(100,999)
        ex='select accno from main where accno=%s;'
        cu1.execute(ex,(accno,))
        if cu1.fetchall()==[]:
            break
    try:
        ex="INSERT INTO main (accno,name,dob,balance,password) VALUES (%s,%s,%s,0,%s)"
        cu1.execute(ex,(accno,name,DOB,passwd))
        cu1.execute("INSERT INTO log VALUES (%s,'account created',NULL,NULL,SYSDATE())",(accno,))
        my.commit()
        cu1.close()
        

        nu.destroy()
        x = 'accountNo: ' + str(accno)
        ne=Toplevel(root)
        ne.title("New Account")
        frm = ttk.Frame(ne, padding=(90,15,90,15))
        frm.grid()
        ttk.Label(frm, text=x).grid(column=0, row=0)
        ttk.Button(frm, text="main page", command=lambda: (ne.destroy(),root.deiconify())).grid(column=0,row=4,columnspan=2)
    except:
        messagebox.showerror('invalid input','values are wrong try again')

def all_accounts():
    global my
    cu=my.cursor()
    cu.execute("select * from main;")
    data=cu.fetchall()
    cu.close()
    return data

def logs():
    global my
    cu=my.cursor()
    cu.execute("select * from log order by date desc;")
    data=cu.fetchall()
    cu.close()
    return data

def scr_account(accno):
    global my
    cu=my.cursor()
    cu.execute("select * from main where accno=%s;",(accno,))
    data=cu.fetchone()
    cu.close()
    return data

def update_acc(accno, name, dob, password):
    global my
    cu=my.cursor()
    cu.execute("update main set name=%s,dob=%s,password=%s where accno=%s;",(name,dob,password,accno))
    my.commit()
    cu.close()
