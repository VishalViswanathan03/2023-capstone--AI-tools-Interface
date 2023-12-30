import speech_recognition as sr
import pyttsx3
import openai
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

from authenticator import api

openai.api_key = api
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
conversation = ""
user_name = "Vishal"
bot_name = "Jarvis"


def start_conversation():
    global conversation
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening")
    try:
        user_input = r.recognize_google(audio)
    except:
        return
    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation += prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()


def stop_conversation():
    engine.stop()


root = ctk.CTk()
root.geometry("500x500")
root.title("AI VOICE ASSISTANT")

label = ctk.CTkLabel(root, text="AI VOICE ASSISTANT")
label.pack()

mic_img = Image.open("mic.jpg")
mic_img = mic_img.resize((100, 100))
mic_photo = ImageTk.PhotoImage(mic_img)

pause_img = Image.open("pause.jpg")
pause_img = pause_img.resize((100, 100))
pause_photo = ImageTk.PhotoImage(pause_img)

# Create the buttons with the resized images
start_button = ctk.CTkButton(root, text="", image=mic_photo,
                             command=start_conversation, width=50, height=50)
stop_button = ctk.CTkButton(root, text="", image=pause_photo,
                            command=stop_conversation, width=50, height=50)

# Pack the buttons
start_button.pack(pady=(100, 20))
stop_button.pack(pady=20)

root.mainloop()
