import customtkinter as ctk
from tkinter import filedialog
from difflib import SequenceMatcher

def checkPlagiarism():
    file1 = open(file1_entry.get())
    file2 = open(file2_entry.get())
    text1 = file1.read()
    text2 = file2.read()
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    if similarity_ratio > 0.6:
        result_label.config(text="Plagiarism detected!")
    else:
        result_label.config(text="No plagiarism detected.")

def browse_file1():
    filename = filedialog.askopenfilename()
    file1_entry.delete(0, ctk.END)
    file1_entry.insert(0, filename)

def browse_file2():
    filename = filedialog.askopenfilename()
    file2_entry.delete(0, ctk.END)
    file2_entry.insert(0, filename)

root = ctk.CTk()
root.geometry("500x500")

file1_label = ctk.CTkLabel(root, text="File 1:")
file1_label.pack()

file1_entry = ctk.CTkEntry(root)
file1_entry.pack()

browse_button_1 = ctk.CTkButton(root, text="Browse", command=browse_file1)
browse_button_1.pack()

file2_label = ctk.CTkLabel(root, text="File 2:")
file2_label.pack()

file2_entry = ctk.CTkEntry(root)
file2_entry.pack()

browse_button_2 = ctk.CTkButton(root, text="Browse", command=browse_file2)
browse_button_2.pack()

check_button = ctk.CTkButton(root, text="Check plagiarism", command=checkPlagiarism)
check_button.pack()

result_label = ctk.CTkLabel(root, text="")
result_label.pack()

root.mainloop()
