from Tkinter import*
from tkMessageBox import*
import os
splash=Tk()
splash.geometry("1400x768+0+0")
splash.configure(background="black")
Label(splash,text="PROJECT DETAILS",fg="red",bg="black",font="candara 40 underline bold").grid(row=2,column=4,columnspan=10)
Label(splash,text="NAME ::ABHISHEK CHAUHAN",fg="red",bg="black",font="none 20").grid(row=3,column=4,columnspan=10)
Label(splash,text="ENROLLMENT NO.::161B294",fg="red",bg="black",font="none 20").grid(row=4,column=4,columnspan=10)
Label(splash,text="BATCH::BZ(B-10)",fg="red",bg="black",font="none 20").grid(row=5,column=4,columnspan=10)
Label(splash,text="PROJECT NAME::",fg="red",bg="black",font="none 20").grid (row=6,column=4,columnspan=10)
def spp(event):
    splash.destroy()
    root=Tk()
    root.configure(background="black")
    root.geometry('1400x768+0+0')
    a=PhotoImage(file="logo.gif")
    Label(root,image=a)
    Label(root,text="BOOK YOUR SHOW",bg="black",fg="red",font="candara 90 bold",padx=170).grid(row=0,column=0,columnspan=10)
    Label(root,text="USER NAME",fg="red",bg="black",font="none 20 bold").grid(row=9,column=3,pady=50)
    l1=Entry(root,bg='white',bd=5,font="none 20 bold")
    l1.grid(row=9,column=5)
    Label(root,text="PASSWORD",fg="red",bg="black",font="none 20 bold",bd=5).grid(row=11,column=3)
    l2=Entry(root,show='*',bd=5,bg='white',font="times 20 bold")
    l2.grid(row=11,column=5)

    def log():
        if l2.get() == "123" and l1.get() == 'abhishek' :
            l2.delete(0,END)
            Label(root,text='Successfull Login').grid()
            os.startfile("pro.py")
        else :
            Label(root,text='Wrong Password').grid()
            

    Button(root,text='Login',command=log,bd=5,font="candara 22 bold",pady=3,padx=5,bg='white').grid(row=13,column=4,padx=10,pady=50,sticky=W+S+N)
    root.mainloop()
lb=Label(splash,text="BOOK YOUR SHOW",bg="black",fg="red",font="candara 90 bold")
lb.bind("<Motion>",spp)
lb.grid(row=7,column=5,columnspan=5,padx=170,pady=3)
splash.mainloop()
