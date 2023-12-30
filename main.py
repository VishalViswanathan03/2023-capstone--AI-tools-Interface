import customtkinter as ctk
from subprocess import call
from PIL import ImageTk, Image
import pygame

root = ctk.CTk()
root.geometry("500x500")
root.title("AI tools")

canvas = ctk.CTkCanvas(root, width=650, height=650)
canvas.pack()

bg_image = Image.open("bg.png")
bg_image = bg_image.resize((650, 650))
bg_image_tk = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

l = ctk.CTkLabel(canvas, text="AI powered productivity tools",
                 font=ctk.CTkFont(weight="bold"), bg_color="#616666")
canvas.create_window(300, 50, window=l)

def img():
    call(["python", "imageGenerator.py"])

B1 = ctk.CTkButton(canvas, text="Image Generator", command=img, width=150,
                   height=50, bg_color="#616666")
canvas.create_window(300, 150, window=B1)

def voice():
    call(["python", "AIvoiceassistant.py"])

B2 = ctk.CTkButton(canvas, text="AI Voice Assistant", command=voice,
                   width=150, height=50, bg_color="#616666")
canvas.create_window(300, 220, window=B2)

def bot():
    import chatbot

B3 = ctk.CTkButton(canvas, text="ChatBot", command=bot, height=50,
                   width=150, bg_color="#616666")
canvas.create_window(300, 290, window=B3)

def grammar():
    import grammarCorrector

B4 = ctk.CTkButton(canvas, text="Grammar Corrector",
                   command=grammar, width=150, height=50, bg_color="#616666")
canvas.create_window(300, 360, window=B4)

def pc():
    import plagiarismChecker

B5 = ctk.CTkButton(canvas, text="Plagiarism checker", command=pc,
                   width=150, height=50, bg_color="#616666")
canvas.create_window(300, 430, window=B5)

def ttos():
    import texttospeech

B6 = ctk.CTkButton(canvas, text="text-to-speech", command=ttos, width=150,
                   height=50, bg_color="#616666")
canvas.create_window(300, 500, window=B6)

def qr():
    import qrgenerator

B7 = ctk.CTkButton(canvas, text="QR Code Generator", command=qr,
                   width=150, height=50, bg_color="#616666")
canvas.create_window(300, 570, window=B7)

pygame.init()
pygame.mixer.music.load("button_sound.mp3")

for button in [B5, B1, B2, B6, B3, B7, B4]:
    button.bind("<Enter>", lambda event: pygame.mixer.music.play())

root.mainloop()
