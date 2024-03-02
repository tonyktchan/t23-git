'''
This is a simple python program to print Hello World!

'''
from datetime import datetime

username = input("What is your name: ")

current_datetime = datetime.now()
week_day = current_datetime.weekday()

print(f"Hello World and {username}!")

day_names =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(f"Today is {day_names[week_day]}.")

