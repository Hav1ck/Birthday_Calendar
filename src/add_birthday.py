import utilities
from json import load, dump
from os.path import join, dirname
from os import getlogin

def add_birthday(json_path):
    while True:
        with open(json_path, "r") as f:
            data = load(f)

        name = input("Enter name: ")
        date = input("Enter date in format dd.mm: ")

        data[name] = date

        with open(json_path, "w") as f:
            dump(data, f)

        print(f"Birthday for {name} added at the date: {date}")

if __name__ == "__main__":
    username = getlogin()
    json_path = 'config/dates.json'
    utilities.file_exist(json_path)
    add_birthday(json_path)
