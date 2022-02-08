from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("HTML file")
root.minsize(650,650)
root.maxsize(650,650)

label_name = Label(root, text="Your file name:")
label_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_name = Entry(root)
input_name.place(relx=0.46, rely=0.03, anchor=CENTER)

my_text = Text(root, width=80, height=35, bg="light slate gray")
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

name = ""

def openFile():
    global name
    my_text.delete(1.0, END)
    input_name.delete(0, END)
    html_file = filedialog.askopenfilename(title="Open HTML File", filetypes=(("html files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split(".")[0]
    input_name.insert(END, formated_name)
    root.title(formated_name)
    html_file = open(name, "r")
    paragraph = text_file.read()
    my_html.insert(END, paragraph)
    html_file.close()

open_button = Button(root, text="Open file", command=openFile)
open_button.place(relx=0.05, rely=0.03, anchor=CENTER)


root.mainloop()