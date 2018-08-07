from tkinter import *
#creating window object
window=Tk()
#define labels
l1=Label(window, text="Company")
l1.grid(row=0,column=0)
l2=Label(window, text="Departments")
l2.grid(row=1,column=0)
l3=Label(window, text="Sections")
l3.grid(row=0,column=2)
l4=Label(window, text="EmpName")
l4.grid(row=1,column=2)
#define entries
Company_text=StringVar()
e1=Entry(window,textvariable=Company_text)
e1.grid(row=0,column=1)

Department_text=StringVar()
e2=Entry(window,textvariable=Department_text)
e2.grid(row=1,column=1)

Sections_text=StringVar()
e3=Entry(window,textvariable=Sections_text)
e3.grid(row=0,column=3)

EmpName_text=StringVar()
e4=Entry(window,textvariable=EmpName_text)
e4.grid(row=1,column=3)

#define listbox

list1=Listbox(window,height=8,width=25)
list1.grid(row=2,column=0,rowspan=2)

#attach scrollbar

scbar1=Scrollbar(window)
scbar1.grid(row=2,column=2,columnspan=2)
list1.configure(yscrollcommand=scbar1.set)
scbar1.configure(command=list1.yview)

#define buttons

b1=Button(window,text="View All",width=12)
b1.grid(row=2,column=3)
b2=Button(window,text="Search",width=12)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",width=12)
b3.grid(row=4,column=3)
b4=Button(window,text="Update",width=12)
b4.grid(row=5,column=3)
b5=Button(window,text="CLose",width=12)
b5.grid(row=6,column=3)
