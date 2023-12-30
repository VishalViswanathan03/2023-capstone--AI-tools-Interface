import customtkinter as ctk
import openai
from tkinter import messagebox
from authenticator import api

openai.api_key = api

def checkGrammar():
    text = textbox.get("1.0", "end-1c")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Correct the following sentence only if there is a major error: {text}",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    corrected = response.choices[0].text
    if corrected == text:
        messagebox.showinfo("Grammar check", "No errors found!")
    else:
        messagebox.showerror("Grammar check", "The corrected statement (if there is an error):\n" + corrected)

root3 = ctk.CTk()
root3.geometry("500x500")
root3.title("Grammar checker-corrector")

textbox = ctk.CTkTextbox(root3, width=400, height=400)
textbox.pack()

button = ctk.CTkButton(root3, text="SUBMIT", command=checkGrammar)
button.pack()

root3.mainloop()
