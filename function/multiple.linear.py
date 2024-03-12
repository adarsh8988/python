import tkinter as tk
import joblib
import sklearn
data=tk.Tk()
data.geometry("500x400")
data.title("Multiple Linear Regression")
# data.config(background="red")


mod=joblib.load("percantage-checker.joblib")

def check():
    marks=en.get()
    marks=float(marks)
    # print(marks)
    
    age=en5.get()
    # print(age)
    
    m=mod.coef_
    # z=m[0,0]
    # x=m[0,1]
    b=mod.intercept_
    # print(m)
    # print(b)

    percentage=b+(m[0,0]*marks)+(m[0,1]*int(age))
    # percentage  =str(percentage)[0 : 4]
    lbl5.config(text=f"{float(percentage)} %.")
    

frame1=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame1.pack()
lbl1=tk.Label(frame1,text="Check Student Percantage",font=("robort",10,"bold"),bg="skyblue")
lbl1.grid(row=1,column=3)
frame2=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue",width=50)
frame2.pack(padx=5,pady=10)

lbl2=tk.Label(frame2,text="Enter Marks",font=("robort",10,"bold"),bg="skyblue")
lbl2.grid(row=2,column=2,pady=10)

lbl7=tk.Label(frame2,text="Student Age",font=("robort",10,"bold"),bg="skyblue")
lbl7.grid(row=3,column=2,pady=10)

lbl3=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl3.grid(row=2,column=3,pady=10)

lbl8=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl8.grid(row=3,column=3,pady=10)


en=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en.grid(padx=10,row=2,column=4,pady=10)
en5=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en5.grid(padx=10,row=3,column=4,pady=10)
# en.pack()

lbl=tk.Button(frame2,text="Check",font=("robort",10,"bold"),bg="red",command=check)
lbl.grid(row=5,column=4,pady=10)
# lbl.pack()

frame3=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame3.pack(pady=10)

lbl4=tk.Label(frame3,text="Your percantage is ",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=1,padx=5,pady=10)
# lbl4.pack()

lbl4=tk.Label(frame3,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=2,padx=5,pady=10)
# lbl4.pack()
lbl5=tk.Label(frame3,text=" ",font=("robort",10,"bold"),bg="skyblue")
lbl5.grid(row=4,column=3,padx=5,pady=10)









data.mainloop()