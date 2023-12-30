import customtkinter as ctk
import openai
from authenticator import api

openai.api_key = api

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def get_response():
    user_input = input_field.get()
    response = generate_response(user_input)
    output_field.insert(ctk.END, "Bot: " + response + "\n")

root1 = ctk.CTk()
root1.title("Multifunctional Chatbot")
root1.geometry("500x500")

output_field = ctk.CTkTextbox(root1, height=300, width=400)
output_field.pack()

button = ctk.CTkButton(root1, text="Send", command=get_response)
button.pack()

input_field = ctk.CTkEntry(root1)
input_field.pack()

root1.mainloop()
