# Password Generator


from tkinter import *
from tkinter.ttk import Combobox
import random
import tkinter as tk

screen=tk.Tk()
screen.title("Password Generator")
screen.geometry("600x400")
screen.configure(background="brown")

def gen():
    global sc1
    sc1.set("")
    passw=" "
    length=int(c1.get())
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mixs="0123456789"+lowercase+uppercase+"@#$%*"

    if c2.get()=="Low Strength":
        for i in range(0,length):
            passw=passw+random.choice(lowercase)
        sc1.set(passw)

    elif c2.get()=="Medium Strength":
        for i in range(0,length):
            passw=passw+random.choice(uppercase)
        sc1.set(passw)

    elif c2.get()=="High Strength":
        for i in range(0,length):
            passw=passw+random.choice(mixs)
        sc1.set(passw)


sc1=tk.StringVar(value="")
t1=Label(screen,text="Python Password Generator",font=("arial",28),fg="red",bg="yellow")
t1.place(x=60,y=0)
t2=Label(screen,text="Password :- ",font=("arial",14))
t2.place(x=145,y=90)

i1=Entry(screen,font=("arial",14),textvariable=sc1)
i1.place(x=255,y=90)


t3=Label(screen,text="Length :- ",font=("arial",14))
t3.place(x=145,y=120)
t4=Label(screen,text="Strength :- ",font=("arial",14))
t4.place(x=145,y=155)

c1=Entry(screen,font=("arial",14),width=15)
c1.place(x=230,y=120)

c2=Combobox(screen,font=("arial",14),width=15)
c2["values"]=("Low Strength","Medium Strength","High Strength")
c2.current(1)
c2.place(x=237,y=155)


b=Button(screen,text="Generate",font=("arial",28),fg="red",bg="white",command=gen)
b.place(x=230,y=195)

screen.mainloop()


