from tkinter import *
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()
root.geometry("300x500")
# root.wm_iconbitmap("C:\\PycharmProjects\\GUI\\nature.png")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue)
screen.pack()
f1 = Frame(root,bg="red")
b1 = Button(f1, text="9")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="8")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="7")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root,bg="red")
b1 = Button(f1, text="6")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="5")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="4")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root,bg="red")
b1 = Button(f1, text="3")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="2")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="1")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root,bg="red")
b1 = Button(f1, text="0")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="-")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="*")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root,bg="red")
b1 = Button(f1, text="/")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="%")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="=")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root,bg="red")
b1 = Button(f1, text="C")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="+")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="*")
b1.pack(side=LEFT)
b1.bind("<Button-1>", click)
f1.pack()

root.mainloop()
