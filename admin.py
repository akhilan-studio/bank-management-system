from tkinter import *
from tkinter import ttk,messagebox
import mysql_connection as m


ADMIN_USER = "admin"
ADMIN_PASS = "1234"

def show_admin_login(root):
    login = Toplevel(root)
    login.title("Admin Login")
    frm = ttk.Frame(login,padding=30)
    frm.grid()

    ttk.Label(frm, text="Username:").grid(column=0,row=0)
    uname = StringVar()
    ttk.Entry(frm, textvariable=uname).grid(column=1,row=0)

    ttk.Label(frm,text="Password:").grid(column=0,row=1)
    passwd = StringVar()
    ttk.Entry(frm,textvariable=passwd,show="*").grid(column=1,row=1)

    ttk.Button(frm,text="Login",command=lambda: (try_login(uname.get(),passwd.get(),root,login))).grid(column=0,row=2,padx=5,pady=5,columnspan=2)
    ttk.Button(frm,text="Cancel",command=login.destroy).grid(column=0,row=3,columnspan=2)

def try_login(uname,passwd,root,login):
    global ADMIN_PASS,ADMIN_USER
    if uname==ADMIN_USER and passwd==ADMIN_PASS:
        root.withdraw()
        login.destroy()
        show_admin_dashboard(root)
    else:
        messagebox.showerror("Login Failed","Invalid admin credentials")
        show_admin_login(root)


def show_admin_dashboard(root):
    dash = Toplevel(root)
    dash.title("Admin Dashboard")
    frm = ttk.Frame(dash,padding=(60,0,60,0))
    frm.grid()

    ttk.Label(frm,text="Admin Dashboard",font=(None, 14)).grid(column=0,row=0)

    ttk.Button(frm,text="View All Accounts",command=lambda:(dash.withdraw(),view_all_accounts(dash))).grid(column=0,row=1,pady=5)
    ttk.Button(frm,text="Search Account",command=lambda:(dash.withdraw(),search_account(dash))).grid(column=0,row=2,pady=5)
    ttk.Button(frm,text="View Transaction Logs",command=lambda:(dash.withdraw(),view_log(dash))).grid(column=0,row=3,pady=5)
    ttk.Button(frm,text="Edit Account Details",command=lambda:(dash.withdraw(),edit_account_page(dash))).grid(column=0,row=4,pady=5)
    ttk.Button(frm,text="Close",command=lambda:(dash.destroy(),root.deiconify())).grid(column=0,row=5,pady=5)




def view_all_accounts(parent):
    win = Toplevel(parent)
    win.title("All Accounts")
    frm = ttk.Frame(win)
    frm.grid()

    colms = ("Accno","Name","DOB","Balance")
    tree = ttk.Treeview(frm,columns=colms,show='headings')
    for c in colms:
        tree.heading(c,text=c)
    tree.grid(row=0,column=0,sticky='nsew')

    sb = ttk.Scrollbar(frm,orient=VERTICAL,command=tree.yview)
    tree.configure(yscroll=sb.set)
    sb.grid(row=0,column=1,sticky='ns')

    accounts = m.all_accounts()
    for a in accounts:
        tree.insert('',END,values=a)

    ttk.Button(frm,text="Back",command=lambda:(win.destroy(),parent.deiconify())).grid(row=1,column=0)




def search_account(parent):
    win = Toplevel(parent)
    win.title("Search Account")
    frm = ttk.Frame(win,padding=30)
    frm.grid()

    ttk.Label(frm, text="Account No:").grid(column=0,row=0)
    acc = StringVar()
    ttk.Entry(frm, textvariable=acc).grid(column=1,row=0)

    result_frame = ttk.Frame(win)
    result_frame.grid(column=0,row=2)

    def do_search():
        if not acc.get().isdigit():
            messagebox.showerror("Invalid","Enter a valid account number")
            return
        data = m.scr_account(acc.get())
        for widget in result_frame.winfo_children():
            widget.destroy()
        if data is None:
            ttk.Label(result_frame,text="Account not found").grid()
        else:
            ttk.Label(result_frame,text=f"Accno:{data[0]}").grid()
            ttk.Label(result_frame,text=f"Name:{data[1]}").grid()
            ttk.Label(result_frame,text=f"DOB:{data[2]}").grid()
            ttk.Label(result_frame,text=f"Balance:{data[4]}").grid()

    ttk.Button(frm,text="Search",command=do_search).grid(column=0,row=1,columnspan=2)
    ttk.Button(frm,text="Back",command=lambda:(win.destroy(),parent.deiconify())).grid(column=0,row=3,padx=10)




def view_log(parent):
    win = Toplevel(parent)
    win.title("Transaction Logs")
    frm = ttk.Frame(win,padding=10)
    frm.grid()

    cols = ("accno","type","amount","transfer recipeint","time")
    tree = ttk.Treeview(frm,columns=cols,show='headings')
    for c in cols:
        tree.heading(c, text=c.title())
    tree.grid(row=0,column=0,sticky='nsew')

    sb = ttk.Scrollbar(frm,orient=VERTICAL,command=tree.yview)
    tree.configure(yscroll=sb.set)
    sb.grid(row=0,column=1,sticky='ns')

    logs = m.logs()
    for l in logs:
        tree.insert('',END,values=l)

    ttk.Button(frm,text="Back",command=lambda:(win.destroy(),parent.deiconify())).grid(row=1,column=0,pady=8)




def edit_account_page(parent):
    win = Toplevel(parent)
    win.title("Edit Account")
    frm = ttk.Frame(win,padding=10)
    frm.grid()

    ttk.Label(frm,text="Account No:").grid(column=0,row=0)
    acc = StringVar()
    ttk.Entry(frm,textvariable=acc).grid(column=1,row=0)

    name_var = StringVar()
    dob_var = StringVar()
    pass_var = StringVar()

    def fetch():
        if not acc.get().isdigit():
            messagebox.showerror("Invalid","Enter a valid account number")
            return
        data = m.scr_account(acc.get())
        if data is None:
            messagebox.showerror("Not found","Account not found")
            return
        name_var.set(data[1])
        dob_var.set(str(data[2]))
        pass_var.set(data[3])

    ttk.Button(frm, text="Load",command=fetch).grid(column=0,row=1,columnspan=2,pady=5)

    ttk.Label(frm, text="Name:").grid(column=0,row=2)
    ttk.Entry(frm, textvariable=name_var).grid(column=1,row=2)

    ttk.Label(frm, text="DOB (YYYY-MM-DD):").grid(column=0,row=3)
    ttk.Entry(frm, textvariable=dob_var).grid(column=1,row=3)

    ttk.Label(frm, text="Password:").grid(column=0,row=4)
    ttk.Entry(frm, textvariable=pass_var).grid(column=1,row=4)

    def save_changes():
        if not acc.get().isdigit():
            messagebox.showerror("Invalid","Enter a valid account number")
            return
        try:
            m.update_acc(acc.get(),name_var.get(),dob_var.get(),pass_var.get())
            messagebox.showinfo("Saved","Account updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update account: {e}")

    ttk.Button(frm, text="Save", command=save_changes).grid(column=0,row=5, columnspan=2,pady=6)
    ttk.Button(frm, text="Back", command=lambda:(win.destroy(),parent.deiconify())).grid(column=0,row=6,columnspan=2)
