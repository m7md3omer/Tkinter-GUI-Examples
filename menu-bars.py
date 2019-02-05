from tkinter import *
from tkinter import messagebox

def get_font(event=None):
    print("selected font is : " + text_font.get())

def quit(event=None):
    root.quit()

def show_about(event=None):
    messagebox.showinfo("about", "about this app")

# ---- VIEW MENU ---
root = Tk()
# create a main_menu
main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
# add file main_menu items
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="DoSome")
# add a seperator line
file_menu.add_separator()
# close the program when this option is clicked
file_menu.add_command(label="Quit", command=quit)

# ------VIEW MENU-----
# create line numbers option
line_numbers = IntVar()
line_numbers.set(1) #checked
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label="line numbers", variable=line_numbers) #add the line number option to the menu

# ----FONT MENU------
text_font = StringVar()
text_font.set("Times")
font_menu = Menu(view_menu, tearoff=0)
font_menu.add_radiobutton(label="Times", variable=text_font, command=get_font)
font_menu.add_radiobutton(label="Courier", variable=text_font, command=get_font)
font_menu.add_radiobutton(label="Ariel ", variable=text_font, command=get_font)
view_menu.add_cascade(label="font", menu=font_menu)

# ----HELP MENU------
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="About", accelerator="ctr+H", command=show_about)
# bind the shortcut Ctrl + H to the show_about function
root.bind("<Control-a>", show_about)
root.bind("<Control-A>", show_about)


# attach the previously created file_menu to the main_menu
main_menu.add_cascade(label="file", menu=file_menu)
# attach the previously created view_menu to the main_menu
main_menu.add_cascade(label="view", menu=view_menu)
# attach the previously created font_menu to the main_menu
main_menu.add_cascade(label="help", menu=help_menu)
# specify the main_menu to the root to use it
root.configure(menu=main_menu)

root.mainloop()