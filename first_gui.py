from tkinter import *
from tkinter import ttk


def handle(event):
    if boolVar.get():
        button.unbind("<Button-1>")
    else:
        button.bind("<Button-1>", get_data)


def get_data(event):
    try:
        print("string = " + strVar.get())
        print("integer = " + str(intVar.get()))
        print("double = " + str(dblVar.get()))
        print("boolean = " + str(boolVar.get()))
        strVar.set("")
        intVar.set("")
        dblVar.set("")
    except Exception as a:
        print(a)


root = Tk()

strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()
strVar.set("")
intVar.set("")
dblVar.set("")
boolVar.set(True)

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)
intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)
dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)
checkButton = Checkbutton(root, text="switch", variable=boolVar)
checkButton.bind("<Button-1>", handle)
checkButton.pack(side=LEFT)

button = Button(root, text="get date")
button.bind("<Button-1>", get_data)
button.pack(side=LEFT)

root.mainloop()
