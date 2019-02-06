from tkinter import *
from tkinter import ttk

class Calculator:

    addButton = False
    subButton = False
    mulButton = False
    divButton = False
    entryValue = 0

    def clear_button_press(self):
        self.entry_val.set("")
        if self.from_equals:
             self.prev = 0.0
             
    def equal_button_press(self):
        self.clear = True
        try:
            if self.mulButton or self.subButton or self.addButton or self.divButton:
                if self.divButton:
                    result = float(self.prev) / float(self.entry_val.get())
                elif self.addButton:
                    result = float(self.prev) + float(self.entry_val.get())
                elif self.subButton:
                    result = float(self.prev) - float(self.entry_val.get())
                elif self.mulButton:
                    result = float(self.prev) * float(self.entry_val.get())

                self.entry_val.set(result)
                self.prev = result
                self.addButton = False
                self.subButton = False
                self.mulButton = False
                self.divButton = False


        except Exception as e:
            print(e)

    def math_button_press(self, value):
        self.equal_button_press()
        print(self.prev)
        self.prev = self.entry_val.get()
        self.addButton = False
        self.subButton = False
        self.mulButton = False
        self.divButton = False
        self.entryValue = 0
        if value == "/":
            self.divButton = True
        elif value == "*":
            self.mulButton = True
        elif value == "+":
            self.addButton = True
        else:
            self.subButton = True


    def button_press(self, value):
        if self.clear:
            self.clear_button_press()
        self.entry_val.set(self.entry_val.get() + value)
        self.clear = False
        self.from_equals = False

    def __init__(self, root):
        self.from_equals = False
        self.prev = 0
        self.entry_val = StringVar()
        self.clear = False

        root.geometry("330x147")
        root.title("Calculator")
        root.resizable(False, False)
        style = ttk.Style()
        style.configure("TEntry", font="Serif", padding=10)
        style.configure("TButton", font="Serif", padding=10)
        style.theme_use("clam")
        style.theme_use("clam")
        self.entry = ttk.Entry(root, textvariable=self.entry_val, width=54)
        self.entry.grid(row=0, columnspan=4)
                    #first row
        ttk.Button(root, text="7", command=lambda: self.button_press("7")).grid(row=1, column=0)
        ttk.Button(root, text="8", command=lambda: self.button_press("8")).grid(row=1, column=1)
        ttk.Button(root, text="9", command=lambda: self.button_press("9")).grid(row=1, column=2)
        ttk.Button(root, text="/", command=lambda: self.math_button_press("/")).grid(row=1, column=3)
                    #second row
        ttk.Button(root, text="4", command=lambda: self.button_press("4")).grid(row=2, column=0)
        ttk.Button(root, text="5", command=lambda: self.button_press("5")).grid(row=2, column=1)
        ttk.Button(root, text="6", command=lambda: self.button_press("6")).grid(row=2, column=2)
        ttk.Button(root, text="*", command=lambda: self.math_button_press("*")).grid(row=2, column=3)
                    #third row
        ttk.Button(root, text="1", command=lambda: self.button_press("1")).grid(row=3, column=0)
        ttk.Button(root, text="2", command=lambda: self.button_press("2")).grid(row=3, column=1)
        ttk.Button(root, text="3", command=lambda: self.button_press("3")).grid(row=3, column=2)
        ttk.Button(root, text="+", command=lambda: self.math_button_press("+")).grid(row=3, column=3)
                    #fourth row
        ttk.Button(root, text="AC", command=self.clear_button_press).grid(row=4, column=0)
        ttk.Button(root, text="0", command=lambda: self.button_press("0")).grid(row=4, column=1)
        ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)
        ttk.Button(root, text="-", command=lambda: self.math_button_press("-")).grid(row=4, column=3)


root = Tk()
calc = Calculator(root)
root.mainloop()