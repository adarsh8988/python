import tkinter as tk
import joblib
import sklearn
import numpy as np
data=tk.Tk()
data.geometry("600x500")
data.title("Logistic Reg.")
# data.config(background="red")


mod=joblib.load("heart_disease_check.joblib")

def check():
    Age=en.get()
#     marks=float(marks)
    # print(Age)
    
    RestingBP=en5.get()
    Cholesterol=en6.get()
    MaxHR=en7.get()
    # print(RestingBP)
    
    zx=np.array([int(Age),int(RestingBP),int(Cholesterol),int(MaxHR)])
    zx.reshape(-1,1)
    # print(zx)
    a=mod.predict([zx])
    lbl5.config(text=f"{(a)}")
   
    
    if a[0]==0:
        print(lbl11.config(text = "You are not suffering from heartdisease"))
    else:
        print(lbl11.config(text = "You are suffering from heartdisease"))
 
frame1=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame1.pack()
lbl1=tk.Label(frame1,text="Check your Heart Disease",font=("robort",10,"bold"),bg="skyblue")
lbl1.grid(row=1,column=3)
frame2=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue",width=50)
frame2.pack(padx=5,pady=10)

lbl2=tk.Label(frame2,text="Enter Age",font=("robort",10,"bold"),bg="skyblue")
lbl2.grid(row=2,column=2,pady=10)

lbl7=tk.Label(frame2,text="Enter your RestingBP",font=("robort",10,"bold"),bg="skyblue")
lbl7.grid(row=3,column=2,pady=10)

lbl8=tk.Label(frame2,text="Enter your Cholesterol",font=("robort",10,"bold"),bg="skyblue")
lbl8.grid(row=4,column=2,pady=10)

lbl8=tk.Label(frame2,text="Enter your MaxHR",font=("robort",10,"bold"),bg="skyblue")
lbl8.grid(row=5,column=2,pady=10)

lbl3=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl3.grid(row=2,column=3,pady=10)

lbl9=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl9.grid(row=4,column=3,pady=10)

lbl8=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl8.grid(row=3,column=3,pady=10)
lbl10=tk.Label(frame2,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl10.grid(row=5,column=3,pady=10)


en=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en.grid(padx=10,row=2,column=4,pady=10)

en5=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en5.grid(padx=10,row=3,column=4,pady=10)

en6=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en6.grid(padx=10,row=4,column=4,pady=10)
en7=tk.Entry(frame2,font=("robort",10,"bold"),width=20)
en7.grid(padx=10,row=5,column=4,pady=10)
# en.pack()

lbl=tk.Button(frame2,text="Check",font=("robort",10,"bold"),bg="red",command=check)
lbl.grid(row=6,column=4,pady=10)
# lbl.pack()

frame3=tk.Frame(data,relief="ridge",borderwidth=10,bg="skyblue")
frame3.pack(pady=10)

lbl4=tk.Label(frame3,text="HeartDisease",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=1,padx=5,pady=10)
# lbl4.pack()

lbl4=tk.Label(frame3,text=":",font=("robort",10,"bold"),bg="skyblue")
lbl4.grid(row=4,column=2,padx=5,pady=10)
# lbl4.pack()
lbl5=tk.Label(frame3,text=" ",font=("robort",10,"bold"),bg="skyblue")
lbl5.grid(row=4,column=3,padx=5,pady=10)
lbl11=tk.Label(frame3,text=" ",font=("robort",10,"bold"),bg="skyblue")
lbl11.grid(row=5,column=2,padx=5,pady=10)


data.mainloop()