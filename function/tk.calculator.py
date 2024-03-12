# calculator
import tkinter as tk

cal=tk.Tk()
cal.geometry("500x500")
cal.config(bg="black")
cal.title("----------CALCULATOR---------")

i=0
equation=""
def show(value):
    global i
    global equation
    if(value=="%"):
        value="/100"
    equation =equation + value
    en1.insert(i,value)
    i=i+1
    


def  clear():
    global equation
    en1.delete(0,"end")
    equation=""

    
def calculate():
    global equation
    result=""
    result= eval(equation)
    
    clear()
    en1.insert(0,result)
    


    

frame1=tk.Frame(cal,relief="ridge",borderwidth=10,bg="gold")
frame1.pack()

lbl=tk.Label(frame1,text="Calculator",font=("robort",10,"bold"),bg="black",fg="red")
lbl.pack()

frame2=tk.Frame(cal,relief="ridge",borderwidth=10,bg="gold")
frame2.pack(pady=10)

en1=tk.Entry(frame2,font=("robort",10,"bold"),width=30,bg="black",fg="red")

en1.pack()

frame3=tk.Frame(cal,relief="ridge",borderwidth=10,width=100,bg="gold")
frame3.pack(pady=10)

lbl1=tk.Button(frame3,text="1",font=("robort",20,"bold"),command=lambda:show("1"),bg="sky blue",fg="red")
lbl2=tk.Button(frame3,text="4",font=("robort",20,"bold"),command=lambda:show("4"),bg="sky blue",fg="red")
lbl3=tk.Button(frame3,text="7",font=("robort",20,"bold"),command=lambda:show("7"),bg="sky blue",fg="red")
lbl4=tk.Button(frame3,text=".",font=("robort",20,"bold"),command=lambda:show("."),bg="sky blue",fg="red")
lbl5=tk.Button(frame3,text="2",font=("robort",20,"bold"),command=lambda:show("2"),bg="sky blue",fg="red")
lbl6=tk.Button(frame3,text="5",font=("robort",20,"bold"),command=lambda:show("5"),bg="sky blue",fg="red")
lbl7=tk.Button(frame3,text="8",font=("robort",20,"bold"),command=lambda:show("8"),bg="sky blue",fg="red")
lbl8=tk.Button(frame3,text="0",font=("robort",20,"bold"),command=lambda:show("0"),bg="sky blue",fg="red")
lbl9=tk.Button(frame3,text="3",font=("robort",20,"bold"),command=lambda:show("3"),bg="sky blue",fg="red")
lbl10=tk.Button(frame3,text="6",font=("robort",20,"bold"),command=lambda:show("6"),bg="sky blue",fg="red")
lbl11=tk.Button(frame3,text="9",font=("robort",20,"bold"),command=lambda:show("9"),bg="sky blue",fg="red")
lbl12=tk.Button(frame3,text="/",font=("robort",20,"bold"),command=lambda:show("/"),bg="sky blue",fg="red")
lbl13=tk.Button(frame3,text="+",font=("robort",20,"bold"),command=lambda:show("+"),bg="sky blue",fg="red")
lbl14=tk.Button(frame3,text="-",font=("robort",20,"bold"),command=lambda:show("-"),bg="sky blue",fg="red")
lbl15=tk.Button(frame3,text="*",font=("robort",20,"bold"),command=lambda:show("*"),bg="sky blue",fg="red")
lbl16=tk.Button(frame3,text="=",font=("robort",20,"bold"),bg="red",command=calculate,width=6,fg="sky blue")
lbl17=tk.Button(frame3,text="C",font=("robort",20,"bold"),command=clear,bg="blue",fg="red")
lbl18=tk.Button(frame3,text="00",font=("robort",20,"bold"),command=lambda:show("00"),bg="sky blue",fg="red")
lbl19=tk.Button(frame3,text="%",font=("robort",20,"bold"),command=lambda:show("%"),bg="sky blue",fg="red")

lbl1.grid(row=1,column=0,padx=10,pady=10)
lbl2.grid(row=2,column=0,padx=10,pady=10)
lbl3.grid(row=3,column=0,padx=10,pady=10)
lbl4.grid(row=4,column=0,padx=10,pady=10)
lbl5.grid(row=1,column=1,padx=10,pady=10)
lbl6.grid(row=2,column=1,padx=10,pady=10)
lbl7.grid(row=3,column=1,padx=10,pady=10)
lbl8.grid(row=4,column=1,padx=10,pady=10)
lbl9.grid(row=1,column=2,padx=10,pady=10)
lbl10.grid(row=2,column=2,padx=10,pady=10)
lbl11.grid(row=3,column=2,padx=10,pady=10)
lbl12.grid(row=4,column=2,padx=10,pady=10)
lbl13.grid(row=1,column=3,padx=10,pady=10)
lbl14.grid(row=2,column=3,padx=10,pady=10)
lbl15.grid(row=3,column=3,padx=10,pady=10)
lbl16.place(x=192,y=240)

lbl17.grid(row=1,column=5,padx=10,pady=10)
lbl18.grid(row=2,column=5,padx=10,pady=10)
lbl19.grid(row=3,column=5,padx=10,pady=10)

cal.mainloop()
