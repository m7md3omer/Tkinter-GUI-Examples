# styling buttons , using themes and showing message dialogues


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def showMsgBox():
    messagebox.showinfo("the title", "hey error")

root = Tk()
root.geometry("400x400+100+100")
root.resizable(False,False)
frame = Frame(root)
style = ttk.Style()
style.configure("TButton",
                forground="midnight blue",
                font="Serif 20 bold italic",
                padding=20)
print(ttk.Style().theme_names())
style.theme_use("clam")
print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "forground"))
print(style.lookup("TButton", "padding"))
button = ttk.Button(frame, text="Stylish button", command=showMsgBox)
# you can also make the button unclickable by the next line
# button["state"] = 'disabled'
button.pack()
frame.pack()

root.mainloop()