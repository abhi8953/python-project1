from Tkinter import*
from tkMessageBox import*
import sqlite3
root=Tk()
global e
global v1
global v2
global price
global priceq
global pricew
global pricep
def booksnow():
    book=Tk()
    def destroy():
        book.destroy()
    Button(book,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=20,column=0)
    book.configure(background="black")
    Label(book,text="Welcome to the counter:",fg="red",bg="black",font="none 50").grid(row=0,column=0)
    Label(book,text="ENTER NAME:",fg="red",bg="black",font="none 20").grid(row=1,column=0)
    e=Entry(book,font='arial 20')
    e.grid(row=2,column=0,columnspan=1)
    Label(book,text="THE NUMBER OF SEATS",fg="red",bg="black",font="none 20").grid(row=3,column=0)
    quantity=Entry(book,font='arial 20')
    quantity.grid(row=4,column=0,columnspan=1)
    Label(book,text="CHOOSE THE TYPE OF TICKET",fg="red",bg="black",font="none 20").grid(row=5,column=0)
    Label(book,text="Silver Rs.100",fg='red',bg='black',font='none 20').grid(row=6)
    Label(book,text="Gold Rs.150",fg='red',bg='black',font='none 20').grid(row=7)
    Label(book,text="Platinum Rs.200",fg='red',bg='black',font='none 20').grid(row=8)
    Label(book,text="entry shold be in capital letters",fg="red",bg="black",font="none 10").grid(row=9)
    quality=Entry(book,font='arial 20')
    quality.grid(row=10,column=0,columnspan=1,pady=10)
    con=sqlite3.Connection('Ticket_DB')
    cur=con.cursor()
    try:
        cur.execute('create table Snowden (Name varchar(25),Quantity int(2),Type varchar(25),Price int(4))')
        con.commit()
    except:
        print ''
    price=100
    def submit():
        if quality.get()=="SILVER":
            price=100
        if quality.get()=="GOLD":
            price=150
        if quality.get()=="PLATINUM":
            price=200
    def Insert():
            a=[e.get(),quantity.get(),quality.get(),price]
            cur.execute('insert into Snowden values(?,?,?,?)',a)
            con.commit()
            showinfo('Good','Successfully Registered')
    Button(book,text="BOOK",width=12,height=2,bd=10,command=Insert).grid(row=11,column=0)
    def show():
        cur.execute('select * from Snowden')
        a=cur.fetchall()
        showinfo('Data',a)
    Button(book,text='Show Customers',width=12,bd=10,height=2,command=show).grid(row=12,columnspan=1)
    book.mainloop()
#-------------------------------------------ticket------------------------------------------------------------------------
def bookjoke():
    book=Tk()
    def destroy():
        book.destroy()
    Button(book,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=20,column=0)
    book.configure(background="black")
    Label(book,text="Welcome to the counter:",fg="red",bg="black",font="none 50").grid(row=0,column=0)
    Label(book,text="ENTER NAME:",fg="red",bg="black",font="none 20").grid(row=1,column=0)
    e=Entry(book,font='arial 20')
    e.grid(row=2,column=0,columnspan=1)
    Label(book,text="THE NUMBER OF SEATS",fg="red",bg="black",font="none 20").grid(row=3,column=0)
    quantity=Entry(book,font='arial 20')
    quantity.grid(row=4,column=0,columnspan=1)
    Label(book,text="CHOOSE THE TYPE OF TICKET",fg="red",bg="black",font="none 20").grid(row=5,column=0)
    Label(book,text="Silver Rs.100",fg='red',bg='black',font='none 20').grid(row=6)
    Label(book,text="Gold Rs.150",fg='red',bg='black',font='none 20').grid(row=7)
    Label(book,text="Platinum Rs.200",fg='red',bg='black',font='none 20').grid(row=8)
    quality=Entry(book,font='arial 20')
    quality.grid(row=9,column=0,columnspan=1,pady=10)
    con=sqlite3.Connection('TicketaDB')
    cur=con.cursor()
    pricep=100
    def submit():
        if quality.get()=="SILVER":
            pricep=100
        if quality.get()=="GOLD":
            pricep=150
        if quality.get()=="PLATINUM":
            pricep=200
    try:
        cur.execute('create table DK(Name varachar(25),Quantity int(2),Type varchar(25),Price int(4))')
        con.commit()
    except:
        print ' '
    def Insert():
            a=[e.get(),quantity.get(),quality.get(),pricep]
            cur.execute('insert into DK values(?,?,?,?)',a)
            con.commit()
            showinfo('Good','Successfully Registered')
            print ''
    Button(book,text="TICKET",width=12,height=2,bd=10,command=Insert).grid(row=11,column=0)
    def show():
        cur.execute('select * from DK')
        a=cur.fetchall()
        showinfo('Data',a)
    Button(book,text='Show Customers',width=12,bd=10,height=2,command=show).grid(row=12,columnspan=1)
    book.mainloop()
def bookwol():
    book=Tk()
    def destroy():
        book.destroy()
    Button(book,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=20,column=0)
    book.configure(background="black")
    Label(book,text="Welcome to the counter:",fg="red",bg="black",font="none 50").grid(row=0,column=0)
    Label(book,text="ENTER NAME:",fg="red",bg="black",font="none 20").grid(row=1,column=0)
    e=Entry(book,font='arial 20')
    e.grid(row=2,column=0,columnspan=1)
    Label(book,text="THE NUMBER OF SEATS",fg="red",bg="black",font="none 20").grid(row=3,column=0)
    quantity=Entry(book,font='arial 20')
    quantity.grid(row=4,column=0,columnspan=1)
    Label(book,text="CHOOSE THE TYPE OF TICKET",fg="red",bg="black",font="none 20").grid(row=5,column=0)
    Label(book,text="Silver Rs.100",fg='red',bg='black',font='none 20').grid(row=6)
    Label(book,text="Gold Rs.150",fg='red',bg='black',font='none 20').grid(row=7)
    Label(book,text="Platinum Rs.200",fg='red',bg='black',font='none 20').grid(row=8)
    quality=Entry(book,font='arial 20')
    quality.grid(row=9,column=0,columnspan=1,pady=10)
    con=sqlite3.Connection('TicketwDB')
    cur=con.cursor()
    priceq=100
    def submit():
        if quality.get()=="SILVER":
            priceq=100
        if quality.get()=="GOLD":
            priceq=150
        if quality.get()=="PLATINUM":
            priceq=200
    try:
        cur.execute('create table Wolverine(Name varchar(25),Quantity int(2),Type varchar(25),Price int(4))')
        con.commit()
    except:
        print ''
    def Insert():
            a=[e.get(),quantity.get(),quality.get(),priceq]
            cur.execute('insert into Wolverine values(?,?,?,?)',a)
            con.commit()
            showinfo('Good','Successfully Registered')
    Button(book,text="BOOK",width=12,height=2,bd=10,command=Insert).grid(row=11,column=0)
    def show():
        cur.execute('select * from Wolverine')
        a=cur.fetchall()
        showinfo('Data',a)
    Button(book,text='Show Customers',width=12,bd=10,height=2,command=show).grid(row=12,columnspan=1)
    book.mainloop()
def bookdead():
    book=Tk()
    def destroy():
        book.destroy()
    Button(book,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=20,column=0)
    book.configure(background="black")
    Label(book,text="Welcome to the counter:",fg="red",bg="black",font="none 50").grid(row=0,column=0)
    Label(book,text="ENTER NAME:",fg="red",bg="black",font="none 20").grid(row=1,column=0)
    e=Entry(book,font='arial 20')
    e.grid(row=2,column=0,columnspan=1)
    Label(book,text="THE NUMBER OF SEATS",fg="red",bg="black",font="none 20").grid(row=3,column=0)
    quantity=Entry(book,font='arial 20')
    quantity.grid(row=4,column=0,columnspan=1)
    Label(book,text="CHOOSE THE TYPE OF TICKET",fg="red",bg="black",font="none 20").grid(row=5,column=0)
    Label(book,text="Silver Rs.100",fg='red',bg='black',font='none 20').grid(row=6)
    Label(book,text="Gold Rs.150",fg='red',bg='black',font='none 20').grid(row=7)
    Label(book,text="Platinum Rs.200",fg='red',bg='black',font='none 20').grid(row=8)
    quality=Entry(book,font='arial 20')
    quality.grid(row=9,column=0,columnspan=1,pady=10)
    con=sqlite3.Connection('TicketpDB')
    cur=con.cursor()
    try:
        cur.execute('create table Deadpool(Name varchar(25),Quantity int(2),Type varchar(25),Price int(4))')
        con.commit()
    except:
        print ''
    pricew=100
    def submit():
        if quality.get()=="SILVER":
            pricew=100
        if quality.get()=="GOLD":
            pricew=150
        if quality.get()=="PLATINUM":
            pricew=200
    def Insert():
        try:
            a=[e.get(),quantity.get(),quality.get(),pricew]
            cur.execute('insert into Deadpool values(?,?,?,?)',a)
            con.commit()
            showinfo('Good','Successfully Registered')
        except:
            print ''
    Button(book,text="BOOK",width=12,height=2,bd=10,command=Insert).grid(row=11,column=0)
    def show():
        cur.execute('select * from Deadpool')
        a=cur.fetchall()
        showinfo('Data',a)
    Button(book,text='Show Customers',width=12,bd=10,height=2,command=show).grid(row=12,columnspan=1)
    book.mainloop()
#--------------------------------------------fifth window------------------------------------------------------------------
def dark():
    knight=Tk()
    def destroy():
        knight.destroy()
    Button(knight,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=9,column=0)
    knight.configure(background="black")
    knight.title("Details")
    Label(knight,text="BOOK YOUR SHOW",fg="red",bg="black",font="candara 70 bold").grid(row=0,column=0)
    Label(knight,text="Details:",fg="red",bg="black",font="none 20 bold").grid(row=1,column=0)
    Label(knight,text="MOVIE TYPE:Action",fg="white",bg="black",font="none 20").grid(row=2,column=0)
    Label(knight,text="DISCRIPTION:",fg="white",bg="black",font="none 20").grid(row=3,column=0)
    Label(knight,text="This movie is based on the person who is the billonare and saves the city from the ",fg="white",bg="black",font="none 15").grid(row=4,column=0)
    Label(knight,text="the crazy and dangerous villian JOKER who plays the major part in the movie",fg="white",bg="black",font="none 15").grid(row=5,column=0)
    Label(knight,text="and tries to kill thee city people and takes revenge from the dark knight.",fg="white",bg="black",font="none 15").grid(row=6,column=0)
    Label(knight,text="RATINGS:8.0/10",fg="white",bg="black",font="none 20").grid(row=7,column=0)
    Button(knight,text="BOOK NOW",width=12,height=5,bd=10,bg="white",command=bookjoke).grid(row=8,column=0)
    knight.mainloop()
#----------------------------------------------fourth window-----------------------------------------------------------------
def deadpool():
    dead=Tk()
    def destroy():
        dead.destroy()
    Button(dead,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=8,column=0)
    dead.configure(background="black") 
    dead.title("Details")
    Label(dead,text="BOOK YOUR SHOW",fg="red",bg="black",font="candara 70 bold").grid(row=0,column=0)
    Label(dead,text="Details:",fg="red",bg="black",font="none 20 bold").grid(row=1,column=0)
    Label(dead,text="MOVIE TYPE:Action",fg="white",bg="black",font="none 20").grid(row=2,column=0)
    Label(dead,text="DISCRIPTION:",fg="white",bg="black",font="none 20").grid(row=3,column=0)
    Label(dead,text="This movie is based on the life of a person whose body is experimentsd by a psycopath",fg="white",bg="black",font="none 15").grid(row=4,column=0)
    Label(dead,text="and gains supernatural abilities and fights for the innnocent",fg="white",bg="black",font="none 15").grid(row=5,column=0)
    Label(dead,text="and saves the life and takes revenge wuth the main villian for his condition.",fg="white",bg="black",font="none 15").grid(row=6,column=0)
    Label(dead,text="RATINGS:8.0/10",fg="white",bg="black",font="none 20").grid(row=7,column=0)
    Button(dead,text="BOOK NOW",width=12,height=5,bd=10,bg="white",command=bookdead).grid(row=8,column=0)
    dead.mainloop()
#-----------------------------------------------third window-----------------------------------------------------------------------
def wolverine():
    wolf=Tk()
    def destroy():
        wolf.destroy()
    Button(wolf,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=9,column=0)
    wolf.configure(background="black")
    wolf.title("Details")
    Label(wolf,text="BOOK YOUR SHOW",fg="red",bg="black",font="candara 70 bold").grid(row=0,column=0)
    Label(wolf,text="Details:",fg="red",bg="black",font="none 20 bold").grid(row=1,column=0)
    Label(wolf,text="MOVIE TYPE:Science and Fiction",fg="white",bg="black",font="none 20").grid(row=2,column=0)
    Label(wolf,text="DISCRIPTION:",fg="white",bg="black",font="none 20").grid(row=3,column=0)
    Label(wolf,text="This movie is based on the lives of the people who were experimented by the scientists and describes",fg="white",bg="black",font="none 15").grid(row=4,column=0)
    Label(wolf,text="how the these people with differenet supernatural abilities survive on the earth",fg="white",bg="black",font="none 15").grid(row=5,column=0)
    Label(wolf,text="irrespective of the neglection from the human community.",fg="white",bg="black",font="none 15").grid(row=6,column=0)
    Label(wolf,text="RATINGS:7.5/10",fg="white",bg="black",font="none 20").grid(row=7,column=0)
    Button(wolf,text="BOOK NOW",width=12,height=5,bd=10,bg="white",command=bookwol).grid(row=8,column=0)
    wolf.mainloop()
#-------------------------------------------------second window------------------------------------------------------------------------
def snowden():
    snow=Tk()
    def destroy():
        snow.destroy()
    Button(snow,text="BACK",width=12,height=3,bd=10,command=destroy).grid(row=9,column=0)
    snow.configure(background="black")
    snow.title("Details")
    Label(snow,text="BOOK YOUR SHOW",fg="red",bg="black",font="candara 70 bold").grid(row=0,column=0)
    Label(snow,text="Details:",fg="red",bg="black",font="none 20 bold").grid(row=1,column=0)
    Label(snow,text="MOVIE TYPE:Hacking",fg="white",bg="black",font="none 20").grid(row=2,column=0)
    Label(snow,text="DISCRIPTION:",fg="white",bg="black",font="none 20").grid(row=3,column=0)
    Label(snow,text="This movie is based on the life of a person who was a cyber security analyst in NSA",fg="white",bg="black",font="none 15").grid(row=4,column=0)
    Label(snow,text="and was found guilty of being leaking the secret information of american government",fg="white",bg="black",font="none 15").grid(row=5,column=0)
    Label(snow,text="to russia and other nations.After that hea started living in Russia.",fg="white",bg="black",font="none 15").grid(row=6,column=0)
    Label(snow,text="RATINGS:9.8/10",fg="white",bg="black",font="none 20").grid(row=7,column=0)
    Button(snow,text="BOOK NOW",width=12,height=5,bd=10,bg="white",command=booksnow).grid(row=8,column=0)
    snow.mainloop()
    
#--------------------------------------------------first window-------------------------------------------------------------------------
def firstly():
    first=Tk()
    def destroy():
        first.destroy()
    Button(first,text="BACK",width=11,height=2,bd=2,bg="white",command=destroy).grid(row=7,column=0)
    first.configure(background="black")
    first.title("booking window")
    Label(first,text="BOOK YOUR SHOW",fg="red",font="candara 70 bold",bg="black").grid(row=0,column=0,columnspan=10)
    Label(first,text="films available for booking:-",fg="red",font="none 20",bg="black").grid(row=1,column=0)
    Button(first,text="Snowden",width=11,height=2,bd=2,bg="white",command=snowden).grid(row=3,column=0)
    Button(first,text="Wolverine",width=11,height=2,bd=2,bg="white",command=wolverine).grid(row=4,column=0)
    Button(first,text="Deadpool",width=11,height=2,bd=2,bg="white",command=deadpool).grid(row=5,column=0)
    Button(first,text="The Dark knight",width=11,height=2,bd=2,bg="white",command=dark).grid(row=6,column=0)
    Label(first,text="For more details click on the movie name",fg="red",bg="black",font="candara 20").grid(row=4,column=1)
    first.mainloop()      
#--------------------------------------------------root window-------------------------------------------------------------------------
root.configure(background="black")
root.title("movie ticket")
Label(root,text="BOOK YOUR SHOW",fg="red",font="candara 70 bold",bg="black").grid(row=0,column=0,columnspan=10)
photo=PhotoImage(file="logo.gif")
Label(root,image=photo).grid(row=1,column=1)
Label(root,text="TO ENTER THE MAIN PORTAL PLAEASE PRESS ENTER",fg="red",font="none 20 bold",bg="black").grid(row=4,column=1)
Button(root,text="ENTER",width=12,height=3,bd=8,command=firstly).grid(row=5,column=1)




    
root.mainloop()


