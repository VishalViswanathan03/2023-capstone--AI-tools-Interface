from customtkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

win = CTk()
win.geometry("500x500")

entry = CTkEntry(win)
entry.pack(pady=20)

def create():
    input = filedialog.asksaveasfilename(title="Save Image", filetypes=(("PNG File", ".png"), ("All Files", "*")))

    if input.endswith(".png"):
        code = pyqrcode.create(entry.get())
        code.png(input, scale=5)
    else:
        input = f'{input}.png'
        code = pyqrcode.create(entry.get())
        code.png(input, scale=5)

    global image_get
    image_get = ImageTk.PhotoImage(Image.open(input))
    label.configure(image=image_get)
    entry.delete(0, END)
    entry.insert(0, "Done!")

def clear():
    entry.delete(0, END)
    label.configure(image='')

button = CTkButton(win, text="Create", command=create)
button.pack(pady=20)

button2 = CTkButton(win, text="Clear", command=clear)
button2.pack()

label = CTkLabel(win, text="")
label.pack(pady=20)

win.mainloop()
