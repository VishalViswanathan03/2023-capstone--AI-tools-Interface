import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from authenticator import api
import openai

openai.api_key = api

root = tk.Tk()
root.geometry("550x650")
root.title("Text-to-Image Generator")

main_image = tk.Canvas(root, width=512, height=512)
main_image.place(x=10, y=110)

promt_input = ctk.CTkEntry(root, height=40, width=512, placeholder_text="Enter a prompt ")
promt_input.place(x=10, y=10)

def apply_dalle():
    global image_
    global img
    prompt = promt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    image_ = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=image_)

def save_image():
    prompt = promt_input.get().replace(" ", "_")
    img.save(f"{prompt}.png")

dalle_button = ctk.CTkButton(root, height=40, width=120, command=apply_dalle)
dalle_button.configure(text="Create")
dalle_button.place(x=110, y=80)

save_button = ctk.CTkButton(root, height=40, width=120, command=save_image)
save_button.configure(text="Save image")
save_button.place(x=270, y=80)

root.mainloop()
