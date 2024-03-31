# Recycling software

from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import time
import random
from tkinter import ttk
from datetime import date
from datetime import datetime
import math
import qrcode
import mysql.connector as m


root = Tk()
root.title("E-Quo - A Mineral Recycling Application from E-Waste - Smart India Hackathon 2022")
bg_color = 'Black'
root.geometry("1215x700")
root.resizable(0, 0)

# Variable Used
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
# Rate = IntVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))

global l
l = []

# Date and Time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# Functions


def datastore():
    f1 = open('mineral.txt', 'r')
    r = f1.readline()
    f1.close()
    f2 = open('quantity.txt', 'r')
    rr = f2.readline()
    ntg = "'"
    t = ntg+T1.get()+ntg
    p = ntg+c_phone.get()+ntg
    n = ntg+c_name.get()+ntg
    r = ntg+r+ntg
    rr = ntg+rr+ntg
    d = str(date.today())
    dd = ntg+d+ntg
    f2.close()
    q = "insert into minerals values({},{},{},{},{},{},{},{})".format(bill_no.get(), t, p, n, r, rr, sum(l)-mis, dd)
    cur.execute(q)
    con.commit()


def help():

    win = Tk()
    win['bg'] = 'ivory'
    # Define the geometry of the window
    win.geometry("260x300")

    frame = Frame(win, width=260, height=300)
    frame.pack()

    # Create a Label Widget to display the text or Image
    hello = tk.Label(frame, text='For any queries or customer support:\n Call or Whatsapp: 94XXXXXX95\nEmail: equocustomer.support@gmail.com\n\nFeedback:')
    hello.place(x=15, y=0)

    ft = tk.Entry(frame, bd=5)
    ft.place(x=10, y=85, width=240, height=175)

    def submitf():
        tt = open("feedback.txt", "a")
        tt.write(T1.get())
        tt.write('\n\n')
        tt.write(ft.get())
        tt.write('\n\n\n')
        tt.close()
        messagebox.showinfo('Feedback', 'Feedback Submitted!')
        win.destroy()

    def clo():
        win.destroy()

    subb = Button(frame, text='Submit', font=("Arial", 8), command=submitf, bg='ivory', bd=1)
    subb.place(x=200, y=270)

    clo = Button(frame, text='Close', font=("Arial", 8), command=clo, bg='ivory', bd=1)
    clo.place(x=150, y=270)

    win.mainloop()


def show():
    t = clicked.get()
    labels.config(text=optionss[t], font=('times new roman', 18, 'bold'))


def remvcha():
    text = "Choose Mineral"
    if clicked.get() == text:
        messagebox.showinfo('Error', 'Please select mineral')
    else:
        additm()


def remvchg():
    text = "Choose Mineral"
    if clicked.get() == text:
        messagebox.showinfo('Error', 'Please select mineral')
    else:
        gbill()


def additm():
    if type(n_txt.get()) == str:
        try:
            qq = float(n_txt.get())
            if type(float(qq)) != float:
                messagebox.showinfo('Error', 'Please enter quantity!\n(Numeric Value)')
            else:
                t = clicked.get()
                qq = float(n_txt.get())
                if t != 'Choose Mineral':
                    if qq != '':
                        show()
                        tt = optionss[t]
                        # n = Rate.get()
                        def tempdatastore():
                            f1 = open('mineral.txt', 'a')
                            f1.write(clicked.get())
                            f1.write(',')
                            f1.close()
                            f2 = open('quantity.txt', 'a')
                            f2.write(n_txt.get())
                            f2.write(',')
                            f2.close()
                        tempdatastore()
                        m = qq * tt
                        l.append(m)
                        if clicked.get() != '':
                            textarea.insert((10.0 + float(len(l) - 1)), f"{clicked.get()}\t\t{n_txt.get()}\t\t{m}\n")
                        else:
                            messagebox.showinfo('Error', 'Please Select Mineral!')
                    else:
                        messagebox.showinfo('Error', 'Please enter quantity!')
        except:
            messagebox.showinfo('Error', 'Please enter quantity!\n(Numeric Value)')
    else:
        t = clicked.get()
        q = n_txt.get()
        if t != 'Choose Mineral':
            if q != '':
                show()
                tt = optionss[t]
                # n = Rate.get()
                m = n_txt.get() * tt
                l.append(m)
                if clicked.get() != '':
                    textarea.insert((10.0 + float(len(l) - 1)), f"{clicked.get()}\t\t{n_txt.get()}\t\t{m}\n")
                else:
                    messagebox.showinfo('Error', 'Please Select Mineral!')
            else:
                messagebox.showinfo('Error', 'Please enter quantity!')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer/Product details not entered")
    else:
        global mis
        mis = round((10 / 100) * sum(l))
        textAreaText = textarea.get(10.0, (10.0 + float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END,
                        f"-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t        SUB TOTAL :Rs. {sum(l)}")
        textarea.insert(END, f"\n\t          MISCELLANEOUS CHARGES:Rs. {mis}")
        textarea.insert(END,
                        f"\n-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t    GRAND TOTAL :Rs. {sum(l) - mis}")
        textarea.insert(END,
                        f"\n-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t Address for the recycle dump:")
        textarea.insert(END, f"\n\t\t#245 Church Street, Bangalore")
        textarea.insert(END, f"\n\n\t   THANK YOU FOR PROMOTING RECYCLING")
        textarea.insert(END, f"\n\t\t\tGO GREEN!")
        datastore()


def clear():
    c_name.set('')
    c_phone.set('')
    clicked.set('Choose Mineral')
    # Rate.set(0)
    labels.config(text='-', font=('times new roman', 18, 'bold'))
    f1 = open('mineral.txt','w')
    f1.close()
    f2 = open('quantity.txt','w')
    f2.close()
    q = "delete from minerals where bill_no={}".format(bill_no.get())
    cur.execute(q)
    con.commit()
    welcome()


def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        cname_lbl.destroy()
        cname_txt.destroy()
        cphone_lbl.destroy()
        cphone_txt.destroy()
        itm.destroy()
        drop.destroy()
        rate.destroy()
        rate_txt.destroy()
        labels.destroy()
        n.destroy()
        n_txt.destroy()

        labelss.place(x=-2, y=0)
        root.after(5000, root.destroy)


def knowaboutdevice():

    # Creating app window
    app = Tk()
    app['bg'] = 'ivory'

    # Defining title of the app
    app.title("GUI Application of Python")

    # Defining label of the app and calling a geometry
    # management method i.e, pack in order to organize
    # widgets in form of blocks before locating them
    # in the parent widget
    ttk.Label(app, text="Know about your device").pack()

    # Creating treeview window
    treeview = ttk.Treeview(app)

    # Calling pack method on the treeview
    treeview.pack()

    # Inserting items to the treeview
    # Inserting parent
    treeview.insert('', '0', 'item1', text='Select you device.')

    # Inserting child
    treeview.insert('', '1', 'item2', text='Laptop')
    treeview.insert('', '2', 'item3', text='Mobile')
    treeview.insert('', 'end', 'item4', text='Camera')

    # Inserting more than one attribute of an item
    treeview.insert('item2', 'end', 'Aluminium - 20g', text='Aluminium - 20g')
    treeview.insert('item2', 'end', 'Copper - 20g', text='Copper - 20g')
    treeview.insert('item3', 'end', '2018 paper', text='Aluminium - 20g')
    treeview.insert('item3', 'end', '2019 paper', text='Copper - 20g')
    treeview.insert('item4', 'end', 'Python', text='Aluminium - 20g')
    treeview.insert('item4', 'end', 'Java', text='Copper - 20g')

    # Placing each child items in parent widget
    treeview.move('item2', 'item1', 'end')
    treeview.move('item3', 'item1', 'end')
    treeview.move('item4', 'item1', 'end')

    # Calling main()
    app.mainloop()


def save_bill():
    text_file = open("test.txt", "w")
    text_file.write(textarea.get(1.0, END))
    text_file.close()
    messagebox.showinfo("Save Successfull! ", "Your bill has been saved to the directory")
    qr_code()


def qr_code():
    f = open('test.txt')
    data = f.read()
    img = qrcode.make(data)
    img.save("secret.png")
    # Import required libraries

    # Create an object of tkinter ImageTk
    filename = "secret.png"
    img = Image.open(filename)
    img.show()


def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t              Exotic Recycler's India Pvt. Ltd. ")
    textarea.insert(END, "\n\t\tMG Road, Bangalore-560001")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END, f"\nBill Number\t\t: {bill_no.get()}")
    textarea.insert(END, f"\nDate\t\t: {date.today()}\t     Time: {current_time}")
    textarea.insert(END, f"\nProduct Name \t\t: {c_name.get()}\t          Customer Name: {c_phone.get()}")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END, "\nMineral Name\t\tMineral Quantity\t\tTotal Price(INR)")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------\n")
    textarea.configure(font='arial 11')


##------------------------------------------- Variables to be placed ------------------------------------------------##

# logo_pic
photo = PhotoImage(file="user&pass_pic .png")  # bg_pic
label = tk.Label(image=photo)
label.img = photo
lphoto = PhotoImage(file="ntg.png")  # logoooo
llabel = tk.Label(image=lphoto, bd=0)
llabel.img = lphoto

# FirstPage
border = tk.LabelFrame(root, text='Login', bg='ivory', bd=1, font=("Arial", 20))
L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
T1 = tk.Entry(border, width=30, bd=5)
L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
T2 = tk.Entry(border, width=30, show='*', bd=5)

# register
border2 = tk.LabelFrame(root, text='Register', bg='ivory', bd=1, font=("Arial", 20))
l1 = tk.Label(border2, text="Username", font=("Arial Bold", 15), bg="ivory")
t1 = tk.Entry(border2, width=30, bd=5)
l2 = tk.Label(border2, text="Password", font=("Arial Bold", 15), bg="ivory")
t2 = tk.Entry(border2, width=30, show="*", bd=5)
l3 = tk.Label(border2, text="Confirm Password   ", font=("Arial Bold", 15), bg="ivory")
t3 = tk.Entry(border2, width=30, show="*", bd=5)

# SecondPage

Label = tk.Label(root, text='''\nDear User,  

        Thank you for choosing E-Quo Recycling Software.\t

    INSTRUCTIONS FOR USING THE APP\t
    1. Enter the name of device that is to be recycled.\t
     2. Select the mineral(s) present in your device from the dropdown
     3.Enter the quantity of minerals present in your device\t
         Use "KNOW YOUR DEVICE" options, if you do not know the quantity of minerals.
    4. After entering details, click on ADD MINERAL\t
     5. Once your are done with entering all the required details, Click on Generate Bill\t

    Thanks & Regards,\t
    Team e-Recyclers \t
    A program by : Nishant V H, Yakhsita Hansdah\t\n\n''', font=("Arial Bold", 10),
                 bg='ivory', fg='black', bd=10)

# slide1-----------------------------                          ------------------------------
# lable
title = tk.Label(root, pady=2, text="Minerals recycling software from E-Waste", bd=12, bg=bg_color,
                 fg='white', font=('times new roman', 25, 'bold'), relief=GROOVE, justify=CENTER)
F1 = tk.Label(root, bd=7, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color)
# detail entry
cname_lbl = tk.Label(F1, text='Product Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cname_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7)
cphone_lbl = tk.Label(F1, text='Customer Name ', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cphone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone, relief=SUNKEN, bd=7)
btn5 = Button(F1, text='Know your device', font='arial 14 bold', command=knowaboutdevice, bg='#e0b0ff', bd=2)
btn5.place(x=855, y=6)
btn6 = Button(F1, text='Save Bill', font='arial 14 bold', command=save_bill, bg='#e0b0ff', bd=2)
btn6.place(x=1047, y=6)
btn6 = Button(F1, text=' ? ', font='arial 14 bold', command=help, bg='#e0b0ff', bd=2)
btn6.place(x=1151, y=6)
# lable2
F2 = tk.LabelFrame(root, text='Product Details', font=('times new roman', 18, 'bold'), fg='#ffe4e1', bg=bg_color)
# actual detail abt mineral
itm = tk.Label(F2, text='Mineral Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')

# for dropdown
options = [
    "Aluminum",
    "Antimony",
    "Barite",
    "Bauxite",
    "Bentonite",
    "Beryllium",
    "Boron",
    "Cadmium",
    "Chromite",
    "Chromium",
    "Cobalt",
    "Columbium",
    "Copper",
    "Europium",
    "Diamond",
    "Diatomite",
    "Feldspar",
    "Gallium",
    "Germanium",
    "Gold",
    "Graphite",
    "Halite",
    "Indium",
    "Iron",
    "Kaolin",
    "Kyanite",
    "Lanthanides",
    "Lead",
    "Lime",
    "Limestone",
    "Lithium",
    "Manganese",
    "Mercury",
    "Mica",
    "Molybdenum",
    "Nickel",
    "Perlite",
    "Platinum",
    "Quartz",
    "Rhenium",
    "Selenium",
    "Silica",
    "Sillimanite",
    "Silver",
    "Strontium",
    "Talc",
    "Tantalum",
    "Tellurium",
    "Terbium",
    "Titanium",
    "Tin",
    "Trona",
    "Tungsten",
    "Vanadium",
    "Yttrium",
    "Zeolite",
    "Zinc",
    "Zirconium"
]

optionss = {
    "Aluminum": 23,
    "Antimony": 24,
    "Barite": 26,
    "Bauxite": 30,
    "Bentonite": 20,
    "Beryllium": 21,
    "Boron": 22,
    "Cadmium": 29,
    "Chromite": 28,
    "Chromium": 28,
    "Cobalt": 30,
    "Columbium": 27,
    "Copper": 20,
    "Europium": 30,
    "Diamond": 50,
    "Diatomite": 44,
    "Feldspar": 29,
    "Gallium": 24,
    "Germanium": 26,
    "Gold": 35,
    "Graphite": 22,
    "Halite": 25,
    "Indium": 24,
    "Iron": 23,
    "Kaolin": 28,
    "Kyanite": 30,
    "Lanthanides": 22,
    "Lead": 23,
    "Lime": 25,
    "Limestone": 27,
    "Lithium": 28,
    "Manganese": 27,
    "Mercury": 30,
    "Mica": 30,
    "Molybdenum": 27,
    "Nickel": 29,
    "Perlite": 26,
    "Platinum": 39,
    "Quartz": 27,
    "Rhenium": 31,
    "Selenium": 23,
    "Silica": 30,
    "Sillimanite": 28,
    "Silver": 33,
    "Strontium": 30,
    "Talc": 24,
    "Tantalum": 25,
    "Tellurium": 22,
    "Terbium": 25,
    "Titanium": 36,
    "Tin": 27,
    "Trona": 26,
    "Tungsten": 30,
    "Vanadium": 27,
    "Yttrium": 30,
    "Zeolite": 29,
    "Zinc": 25,
    "Zirconium": 30
}

labels = tk.Label(root, text="-", font=('times new roman', 17, 'bold'), bg="white", width=16)

clicked = StringVar()
clicked.set("Choose Mineral")  # initial menu text
drop = OptionMenu(F2, clicked, *options)
# clicked.get() is the item choosen
# itm_txt = tk.Label(F2, width=20, textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7)
drop.config(width=32)

rate = tk.Label(F2, text='Mineral Rate per gram', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')
rate_txt = Entry(F2, width=20, font='arial 15 bold', relief=SUNKEN, bd=7)
n = tk.Label(F2, text='Mineral Quantity (in gram)', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')
n_txt = Entry(F2, width=20, font='arial 15 bold', relief=SUNKEN, bd=7)
F3 = Frame(root, relief=GROOVE, bd=10)
# Bill generation area
bill_title = tk.Label(F3, text='Bill Generation Area', font='arial 15 bold', bd=7, relief=GROOVE)
scrol_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scrol_y)

# temporary file making
f1 = open('mineral.txt', 'w')
f1.close()
f2 = open('quantity.txt', 'w')
f2.close()

# data storing
try:
    con = m.connect(host='localhost', user='root', password='00003101015', database='usermin')
    cur = con.cursor()
except:
    con = m.connect(host='localhost', user='root', password='00003101015')
    cur = con.cursor()
    q = "create database usermin"
    cur.execute(q)
    con = m.connect(host='localhost', user='root', password='00003101015', database='usermin')
    cur = con.cursor()
    q1 = "use usermin"
    q2 = """create table minerals
    (Bill_no int Primary key,
    Username varchar(50),
    Customer varchar(25),
    Product varchar(15),
    Mineral_name varchar(50),
    Quantity varchar(50),
    Total_Price int,
    Date date)"""
    cur.execute(q1)
    cur.execute(q2)


# ending pg
photoss = PhotoImage(file="user&pass_pic .png")  # bg_pic
labelss = tk.Label(image=photoss)
labelss.img = photoss


def slide1():
    root['bg'] = 'ivory'
    label.place_forget()
    Label.place_forget()
    Button1.place_forget()
    Button2.place_forget()

    title.pack(fill=X)

    # Product Frames
    F1.place(x=0, y=80, relwidth=1)

    cname_lbl.grid(row=0, column=0, padx=20, pady=5)
    cname_txt.grid(row=0, column=1, padx=10, pady=5)

    cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
    cphone_txt.grid(row=0, column=3, padx=10, pady=5)

    F2.place(x=20, y=180, width=630, height=500)

    itm.grid(row=0, column=0, padx=30, pady=20)
    # itm_txt.place(x=360, y=22)
    drop.place(x=360, y=22)

    rate.grid(row=1, column=0, padx=30, pady=20)
    rate_txt.grid(row=1, column=1, padx=10, pady=20)
    labels.place(x=388, y=304)

    n.grid(row=2, column=0, padx=30, pady=20)
    n_txt.grid(row=2, column=1, padx=10, pady=20)

    # Bill area
    F3.place(x=700, y=180, width=500, height=500)

    bill_title.pack(fill=X)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()
    # Buttons
    btn1 = Button(F2, text='Add Mineral', font='arial 15 bold', command=remvcha, padx=5, pady=10, bg='#8f00ff',
                  width=15, bd=7)
    btn1.grid(row=3, column=0, padx=10, pady=30)
    btn2 = Button(F2, text='Generate Bill', font='arial 15 bold', command=remvchg, padx=5, pady=10, bg='#8f00ff',
                  width=15, bd=7)
    btn2.grid(row=3, column=1, padx=10, pady=30)
    # btn2a = Button(root, text='Next', font='arial 15 bold', command=qr, padx=2, pady=3, bg='#76ff7a', width=6)
    # btn2a.place(x=950, y=92)
    btn3 = Button(F2, text='Clear', font='arial 15 bold', padx=5, pady=10, command=clear, bg='#8f00ff', width=15, bd=7)
    btn3.grid(row=4, column=0, padx=10, pady=10)
    btn4 = Button(F2, text='Exit', font='arial 15 bold', padx=5, pady=10, command=exit, bg='#8f00ff', width=15, bd=7)
    btn4.grid(row=4, column=1, padx=10, pady=10)


def verify():
    try:
        with open("credential.txt", "r") as f:
            info = f.readlines()
            i = 0
            for e in info:
                u, p = e.split(",")
                if u.strip() == T1.get() and p.strip() == T2.get():
                    i = 1
                    SecondPage()
            if i == 0:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
    except:
        messagebox.showinfo("Error", "Please provide correct username and password!!")
        FirstPage()


def check():
    if t1.get() != "" and t2.get() != "" and t3.get() != "":
        with open("credential.txt", "r") as f:
            info = f.readlines()
            if info == ["\n"]:
                if t2.get() == t3.get():
                    with open("credential.txt", "a") as f:
                        f.write(t1.get() + "," + t2.get() + "\n")
                        messagebox.showinfo("Welcome", "You are registered successfully!!")
                        SecondPage()
                if t2.get() != t3.get():
                    messagebox.showinfo("Error", "Your password didn't get match!!")
            else:
                for e in info:
                    u, p = e.split(",")
                    if u.strip() == t1.get():
                        messagebox.showinfo("Error", "Username Exists!\nEnter a different username.")
                        register()
                    if u.strip() != t1.get():
                        if t2.get() == t3.get():
                            with open("credential.txt", "a") as f:
                                f.write(t1.get() + "," + t2.get() + "\n")
                                messagebox.showinfo("Welcome", "You are registered successfully!!")
                                SecondPage()
                        if t2.get() != t3.get():
                            messagebox.showinfo("Error", "Your password didn't get match!!")
    else:
        messagebox.showinfo("Error", "Please fill the complete field!!")


b1 = tk.Button(border2, text="Submit", bg="#6f2da8", font=("Arial", 15), command=check)


# button variable for Register
def register():
    border.pack_forget()
    L1.place_forget()
    T1.place_forget()
    L2.place_forget()
    T2.place_forget()
    B1.place_forget()
    B2.place_forget()

    border2.pack(fill="both", expand=True, padx=370, pady=225)
    l1.place(x=30, y=10)
    t1.place(x=220, y=10)
    l2.place(x=30, y=60)
    t2.place(x=220, y=60)
    l3.place(x=30, y=110)
    t3.place(x=220, y=110)
    b1.place(x=270, y=153)
    b2.place(x=110, y=153)


"""def ThirdPage():
    vid()

    Button=tk.Button(root, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
    Button.place(x=650, y=450)

    Button=tk.Button(root, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
    Button.place(x=100, y=450)
"""


def logo_pic():
    root['bg'] = 'black'
    llabel.place(x=485, y=165)
    root.after(3000, FirstPage)


def FirstPage():
    llabel.place_forget()
    Label.place_forget()
    Button1.place_forget()
    Button2.place_forget()
    border2.pack_forget()
    l1.place_forget()
    t1.place_forget()
    l2.place_forget()
    t2.place_forget()
    l3.place_forget()
    t3.place_forget()
    b1.place_forget()
    b2.place_forget()

    label.place(x=-2, y=0)
    border.pack(fill="both", expand=True, padx=370, pady=240)
    L1.place(x=64, y=18)
    T1.place(x=194, y=18)
    L2.place(x=64, y=74)
    T2.place(x=194, y=74)

    global B1
    global B2
    B1 = tk.Button(border, text="Sign in", font=("Arial", 15), command=verify)
    B1.place(x=260, y=120)
    B2 = tk.Button(border, text="Register", bg="#e51a4c", font=("Arial", 15), command=register)
    B2.place(x=115, y=120)


Button1 = tk.Button(root, text="Back", font=("Arial", 15), command=FirstPage, bg='ivory', fg='black')
# button variables of Firstpage
Button2 = tk.Button(root, text="Next", font=("Arial", 15), command=slide1, bg='ivory', fg='black')

b2 = tk.Button(border2, text="Login", font=("Arial", 15), command=FirstPage)


# button variable of Register--- since FirstPage needs to be defined first.


def SecondPage():

    border.pack_forget()
    L1.place_forget()
    T1.place_forget()
    L2.place_forget()
    T2.place_forget()
    l1.place_forget()
    t1.place_forget()
    B1.place_forget()
    border2.pack_forget()
    l2.place_forget()
    t2.place_forget()
    l3.place_forget()
    t3.place_forget()
    b1.place_forget()
    B2.place_forget()

    Label.place(x=330, y=180)
    Button1.place(x=470, y=510)
    Button2.place(x=730, y=510)


logo_pic()
root.mainloop()
