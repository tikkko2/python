from tkinter import *

def click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,current+str(number))

def add(plus):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,current+str(plus))

def clear():
    entry.delete(0,END)

def equal():
    current = entry.get()
    num = current.split("+")
    numbers=list(map(int,num))
    reuslt = sum(numbers)
    entry.delete(0,END)
    entry.insert(0,reuslt)



window = Tk()

window.title("calculator")

entry = Entry(window, width=35)
entry.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

but1= Button(window,text="1",padx=40,pady=30,command=lambda:click(1))
but2= Button(window,text="2",padx=40,pady=30,command=lambda:click(2))
but3= Button(window,text="3",padx=40,pady=30,command=lambda:click(3))

but4= Button(window,text="4",padx=40,pady=30,command=lambda:click(4))
but5= Button(window,text="5",padx=40,pady=30,command=lambda:click(5))
but6= Button(window,text="6",padx=40,pady=30,command=lambda:click(6))

but7= Button(window,text="7",padx=40,pady=30,command=lambda:click(7))
but8= Button(window,text="8",padx=40,pady=30,command=lambda:click(8))
but9= Button(window,text="9",padx=40,pady=30,command=lambda:click(9))

but0= Button(window,text="0",padx=40,pady=30,command=lambda:click(0))

but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but0.grid(row=4,column=0)

addButton = Button(window,text="+",padx=40,pady=30,command=lambda:add("+"))
clearButton = Button(window,text="clear", padx=77,pady=30,command=clear)
equalButton = Button(window,text="=",padx=87,pady=30,command=equal)

addButton.grid(row=5,column=0)
clearButton.grid(row=4,column=1,columnspan=2)
equalButton.grid(row=5,column=1,columnspan=2)

window.mainloop()
