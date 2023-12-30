import customtkinter as ctk
import pyttsx3

def speak():
    e = pyttsx3.init()
    e.say(text.get("1.0", "end-1c"))
    e.runAndWait()

root2 = ctk.CTk()
root2.geometry("500x500")
root2.title("Text to Speech")

text = ctk.CTkTextbox(root2, width=400, height=200)
text.pack()

button = ctk.CTkButton(root2, text="Speak", command=speak)
button.pack()

root2.mainloop()
