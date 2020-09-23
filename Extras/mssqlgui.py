import pyodbc as db
from tkinter import *
import re

con = db.connect('DRIVER={SQL Server};'
                 'SERVER=ACE11;'
                 'DATABASE=nikhil;'
                 'uid=sa; pwd=nikhil@1234')

def Add():

    cur=con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))
    
    for x in range(5,len(num)+5): 
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
    
    cur.execute("INSERT INTO Empinfo VALUES(?,?,?)",e1.get(),e2.get(),e3.get())
    con.commit()
    Label(master,text="Record Inserted",justify=LEFT).grid(row=5,column=0,sticky=W)

def show():

    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
    
    cur = con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    b=4 ###########
    for row in cur:
        b=b+1
        Label(master,text=row,justify=LEFT).grid(row=b,column=0,sticky=W)
        
def Delete():

    cur=con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))

    for x in range(5,len(num)+5):
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
    
    def ok():
        
        cur= con.cursor()

        var=e4.get()
        cur.execute("DELETE FROM Empinfo WHERE empId =?",var)
        con.commit()

        Label(master,text="Record Deleted",justify=LEFT).grid(row=6,column=0,sticky=W)
    
    Label(master, text="Enter the ID",justify=LEFT).grid(row=5,column=0,sticky=W)
    e4 = Entry(master)
    e4.grid(row=5,column=1)
    
    b=Button(master,text='ok',command=ok).grid(row=5,column=3,sticky=W+E+N+S,pady=4)

def Update():

    cur=con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))
    
    for x in range(5,len(num)+5):
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
    
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
    
    def ok():
        
        cur=con.cursor()

        ids=e6.get()   
        nams=e7.get()
        adds=e8.get()

        cur.execute("UPDATE Empinfo SET empName =?,empAdd =? WHERE empId =?",nams,adds,ids)
        con.commit()

        Label(master, text="Record is updated",justify=LEFT).grid(row=8,column=0,sticky=W)
   
    Label(master, text="Enter ID",justify=LEFT).grid(row=5,column=0,sticky=W)
    Label(master, text="Enter Name update",justify=LEFT).grid(row=6,column=0,sticky=W)
    Label(master, text="Enter Address to update",justify=LEFT).grid(row=7,column=0,sticky=W)
    
    e6 = Entry(master)
    e7 = Entry(master)
    e8 = Entry(master)
    
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    
    Button(master,text='ok',command=ok).grid(row=5,column=3,sticky=W+E+N+S,pady=4)

def first():

    cur = con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))
    
    for x in range(5,len(num)+5):
       Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
       
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)


    for row in curs:
        break
        
    e1.delete(0, END)
    e1.insert(0,row[0])

    e2.delete(0, END)
    e2.insert(0,row[1])

    e3.delete(0, END)
    e3.insert(0,row[2])

    global n
    n=0
    print(n)
       
    
def last():

    cur = con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))
    for x in range(5,len(num)+5):
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)


    global n
    n=0
    
    for row in curs:
        a=(row[0],row[1],row[2])
        n=n+1

    e1.delete(0, END)
    e1.insert(0,row[0])

    e2.delete(0, END)
    e2.insert(0,row[1])

    e3.delete(0, END)
    e3.insert(0,row[2])

    n=n-1
    print(n)
    
def nexts():

    cur = con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))

    for x in range(5,len(num)+5):
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
    
    global n
    n=n+1
    print(n)

    if(-1<n<len(num)):
        
        e1.delete(0, END)
        e1.insert(0,curs[n][0])

        e2.delete(0, END)
        e2.insert(0,curs[n][1])

        e3.delete(0, END)
        e3.insert(0,curs[1][2])

    else:
        
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        Label(master,text="Out of range",justify=LEFT).grid(row=5,column=0,sticky=W)
        print("out of range")


def prev():

    cur = con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))

    for x in range(5,len(num)+5):
        Label(master,text=" "*50,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=3,sticky=W)
        
    
    global n
    n=n-1
    print(n)

    if(-1<n<len(num)):
        
        e1.delete(0, END)
        e1.insert(0,curs[n][0])

        e2.delete(0, END)
        e2.insert(0,curs[n][1])

        e3.delete(0, END)
        e3.insert(0,curs[1][2])

    else:
        
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        
        Label(master,text="Out of range",justify=LEFT).grid(row=5,column=0,sticky=W)
        print("out of range")

def search():
    
    cur=con.cursor()
    cur.execute('SELECT * from Empinfo ORDER BY empId')

    curs = cur.fetchall()
    num=re.findall(r'\d{1,3}',str(curs))

    for x in range(5,len(num)+5):
        Label(master,text=" "*30,justify=LEFT).grid(row=x,column=0,sticky=W)
        
    Label(master,text=" "*50,justify=LEFT).grid(row=5,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=6,column=1,sticky=W)
    Label(master,text=" "*50,justify=LEFT).grid(row=7,column=1,sticky=W)

    def id_ok():
        
        n=e10.get()
        cur.execute('SELECT * FROM Empinfo WHERE username=? and password=?', user,pwd)
        n=cur.fetchall()

        for row in n:
            
            e1.delete(0, END)
            e1.insert(0,row[0])

            e2.delete(0, END)
            e2.insert(0,row[1])

            e3.delete(0, END)
            e3.insert(0,row[2])

    def name():

        t=e9.get()
        cur.execute('SELECT * FROM Empinfo WHERE empName LIKE ?', t+"%")
        n=cur.fetchall()

        i=[]
        for row in n:
            i.append(row[1])
        print(i)

        v=StringVar(master) 
        v.set("list")
        w=OptionMenu(master,v,*i).grid(row=7,column=2,sticky=W)

        def value():
            z=v.get()

            for row in curs:

                if(row[1]==z):
                    
                    e1.delete(0, END)
                    e1.insert(0,row[0])

                    e2.delete(0, END)
                    e2.insert(0,row[1])

                    e3.delete(0, END)
                    e3.insert(0,row[2])                

        Button(master,text="ok",command=value).grid(row=7,column=3,sticky=W)
               
    
    Label(master,text="Search by Id",justify=LEFT).grid(row=5,column=0,sticky=W)
    e10=Entry(master)
    e10.grid(row=5,column=1)
    Button(master,text="ok",command=id_ok).grid(row=5,column=2,sticky=W)

    Label(master,text="Search by name",justify=LEFT).grid(row=6,column=0,sticky=W)
    e9=Entry(master)
    e9.grid(row=6,column=1)
    Button(master,text="ok",command=name).grid(row=6,column=2,sticky=W)
        
        
#Main Menu
        
master = Tk()
master.title("Emp Info")
n=0

Label(master, text="Id",justify=LEFT).grid(row=0,column=0,sticky=W)
Label(master, text="Name",justify=LEFT).grid(row=1,column=0,sticky=W)
Label(master, text="Address",justify=LEFT).grid(row=2,column=0,sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master,text='Show',command=show).grid(row=3,column=0,sticky=W+E+N+S,pady=4)
Button(master,text="Add",command=Add).grid(row=3,column=1,sticky=W+E+N+S,pady=4)
Button(master,text="Update",command=Update).grid(row=3,column=2,sticky=W+E+N+S,pady=4)
Button(master,text="Delete",command=Delete).grid(row=3,column=3,sticky=W+E+N+S,pady=4)

Button(master,text='First',command=first).grid(row=4,column=0,sticky=W+E+N+S,pady=4)
Button(master,text="Prev",command=prev).grid(row=4,column=1,sticky=W+E+N+S,pady=4)
Button(master,text="Next",command=nexts).grid(row=4,column=2,sticky=W+E+N+S,pady=4)
Button(master,text="last",command=last).grid(row=4,column=3,sticky=W+E+N+S,pady=4)

Button(master,text="search",command=search).grid(row=0,column=2,sticky=E+N+S,pady=4)

Button(master,text="x",fg="red",command=master.destroy).grid(row=0,column=3,sticky=E+N+W+S,pady=4)

mainloop()