# import tkinter as tk 
# def myfun():
#     zx=en.get()
#     ad=2023-int(zx)
#     lbl1.config(text=f"user age is: {ad}")
    
# # #  main is a window
# main=tk.Tk()
# # # geometry is used to size

# main.geometry("500x300")
# main.title("This is a age calculator")
# # # config is used to change the background color
# main.config(background="green")
# # # font used as a tuple for accuracy and fg(foreground) is change the colour of font and bg is used for change the background of font

#Button=tk.Button(main,text="Hello World",font=("robort",30,"italic"),fg="red",bg="black")
# # # add text centre and position and x is a axis and padx is skip the corner size and pady is used to down the fonts
# # position=side
# Button.pack(fill="x",padx=20,pady=20)
# # # Button is used to write text
# # # same property applied
# # # Entry is used to show the entrybox 
# en=tk.Entry(main,font=("robort",20,"italic"))
# en.pack()
# btn=tk.Button(main,text="submit",font=("xyz",15,"bold"),command=myfun)
# btn.pack(pady=20)
# lbl1=tk.Button(main,text="",bg="white")
# lbl1.pack()
# main.mainloop()

import tkinter as tk
import mysql.connector
from tkinter import messagebox
con=mysql.connector.connect(host="localhost",username="root",password="Akarsh!@2001",database="tablename")
curser=con.cursor()
def savedata():
    Name=en1.get()
    Age=en2.get()
    Mobile_number=en3.get()
    email_id=en4.get()
    # curser.execute(f"insert into employee values('{Name}',{Age},'{Mobile_number}','{email_id}')")
    # con.commit()
    en1.delete(0,'end')
    en2.delete(0,'end')
    en3.delete(0,'end')
    en4.delete(0,'end')
    # my.config(text="data saved successfully")
    # my.grid(row=6,column=3)
    
    # messagebox.showinfo("data save","your data saved successfully.")
    
    
    # print("Name","Age","Mobile_number","email_id")
    
file=tk.Tk()

file.geometry("500x400")
file.title("Form")
file.config(background="green")

lbl1=tk.Button(file)
lbl1.grid(row=0,column=0)
lbl=tk.Label(file,text="Name",font=("robort",20,"bold"),bg="green")
lbl.grid(row=1,column=1,padx=20,pady=10)
lbl=tk.Label(file,text=":",font=("robort",20,"bold"),bg="green")
lbl.grid(row=1,column=2)
lbl=tk.Label(file,text=":",font=("robort",20,"bold"),bg="green")
lbl.grid(row=2,column=2)
lbl=tk.Label(file,text=":",font=("robort",20,"bold"),bg="green")
lbl.grid(row=3,column=2)
lbl=tk.Label(file,text=":",font=("robort",20,"bold"),bg="green")
lbl.grid(row=4,column=2)
my=tk.Label(file,text=" ",font=("robort",20,"bold"))
en1=tk.Entry(file,font=("robort",20,"italic"))
en1.grid(row=1,column=3)
lbl2=tk.Label(file,text="Age",font=("robort",20,"bold"),bg="green")
lbl2.grid(row=2,column=1,pady=10)
en2=tk.Entry(file,font=("robort",20,"italic"))
en2.grid(row=2,column=3)
lbl3=tk.Label(file,text="Number",font=("robort",20,"bold"),bg="green")
lbl3.grid(row=3,column=1,pady=10)
en3=tk.Entry(file,font=("robort",20,"italic"))
en3.grid(row=3,column=3)
lbl4=tk.Label(file,text="Email",font=("robort",20,"bold"),bg="green")
lbl4.grid(row=4,column=1,pady=10)
en4=tk.Entry(file,font=("robort",20,"italic"))
en4.grid(row=4,column=3)
btn=tk.Button(file,text="Submit",font=("robort",20,"bold"),bg="red",command=savedata)
btn.grid(row=5,column=3,pady=20)
file.mainloop()

