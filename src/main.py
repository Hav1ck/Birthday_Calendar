import utilities
from json import load
from os import path, getlogin
import time
import customtkinter as ctk
from playsound import playsound

def check_coming_birthday(file):
    with open(file, "r") as f:
        data = load(f)
        for name, date in data.items():
            if time.strftime("%d.%m") == date:
                print(f"{name}'s birthday is coming")
                playsound('resources/beep.mp3')
                show_gui(name)


def show_gui(name):
    app = ctk.CTk() 
    app.title("GUI")
    app.geometry("600x300")

    label = ctk.CTkLabel(app, text=f"{name} has a birthday today", font=("Arial", 44))
    label.pack(expand=True)

    app.mainloop()

if __name__ == "__main__":
    username = getlogin()
    json_path = 'config/dates.json'
    utilities.file_exist(json_path)
    check_coming_birthday(json_path)
