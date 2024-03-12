import tkinter as tk
from PIL import Image ,ImageTk

window=tk.Tk()
window.geometry("500x500")
window.title("Frames")
window.config(background="red")

# for show image
img="E:\instagram post\post.png"
x=Image.open(img)
y=ImageTk.PhotoImage(x)
lbl2=tk.Label(window,image=y,height=200,width=200)
lbl2.pack()

frame1=tk.Frame(window,relief="groove",borderwidth=20)
frame1.pack()

frame2=tk.Frame(window,relief="raised",borderwidth=20)
frame2.pack()

lbl=tk.Label(frame1,text="Name",font=("robort",20,"bold"))
lbl.pack()

lbl1=tk.Label(frame2,text="hlo",font=("robort",20,"bold"))
lbl1.pack()

en1=tk.Entry(frame2,font=("robort",20,"bold"))
en1.pack()


window.mainloop()