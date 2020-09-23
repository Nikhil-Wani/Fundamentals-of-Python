from tkinter import *
master = Tk()

#Create & Co
Grid.rowconfigure(master, 0, weight=1)
Grid.columnconfigure(master, 0, weight=1)

#Create & Configure frame 
frame=Frame(master)
frame.grid(row=7, column=0, sticky=N+S+E+W)
        
master.title("Student Info")

#entry name rollno
Label(master, text="Name",justify=LEFT).grid(row=0,column=0,sticky=W)
Label(master, text="rollno",justify=LEFT).grid(row=1,column=0,sticky=W)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Radiobuttons gender
v=IntVar()
Label(master,text="Gender").grid(row=2, column=0, sticky=W, pady=4)
Radiobutton(master,text="Male",padx=20,variable=v,value=3).grid(row=2, column=1, sticky=W, pady=4)
Radiobutton(master,text="Female",padx=20,variable=v,value=4).grid(row=2, column=2, sticky=W, pady=4)

#entry age
Label(master,text="Age").grid(row=3,column=0,stick=W,pady=4)
e3 = Entry(master)
e3.grid(row=3, column=1)

#checkbox
Label(master,text="Hobbies").grid(row=4,column=0,stick=W,pady=4)
v1=IntVar()
Checkbutton(master, text="Travelling", variable=v1).grid(row=4,column=1,sticky=W)
v2 = IntVar()
Checkbutton(master, text="Sketching", variable=v2).grid(row=4,column=2,sticky=W)
v3=IntVar()
Checkbutton(master, text="Sports", variable=v3).grid(row=5,column=1,sticky=W)
v4 = IntVar()
Checkbutton(master, text="Reading", variable=v4).grid(row=5,column=2,sticky=W)

#Dropdown
Label(master,text="Qualification").grid(row=6,column=0,stick=W,pady=4)
OPTIONS = [
"SSC",
"HSC",
"BE",
"BSC"
]
var = StringVar(master)
var.set(OPTIONS[0])
w = OptionMenu(master, var,*Options).grid(row=6,column=1,sticky=W,pady=4)

#buttons
def show_entry_fields():
   print("First Name: %s\nRollno: %s" % (e1.get(), e2.get()))
   
   if(v.get()==3):
       print("Gender:Male")
   else:
       print("Gender:Female")

   print("Age: %s" % (e3.get()))
   
   print("Hobbies:")
   
   if(v1.get()==1):
       print("\tTravelling")
   if(v2.get()==1):
       print("\tSketching") 
   if(v3.get()==1):
       print("\tSports")
   if(v4.get()==1):
       print("\tReading")

   print("Qualification:",var.get())
   
def deleted():
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   
for row_index in range(5):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(10):
        Grid.columnconfigure(frame, col_index, weight=1) 
   
        btn=Button(frame,text='Show',command=show_entry_fields).grid(row=7,column=0,sticky=W+E+N+S,pady=4)
        btn=Button(frame,text="Add").grid(row=7,column=1,sticky=W+E+N+S,pady=4)
        btn=Button(frame,text="Update").grid(row=7,column=2,sticky=W+E+N+S,pady=4)
        btn=Button(frame,text="Delete",command=deleted).grid(row=7,column=3,sticky=W+E+N+S,pady=4)
        btn=Button(frame,text="Close",fg="red",command=master.destroy).grid(row=7,column=4,sticky=W+E+N+S,pady=4)
    

mainloop( )