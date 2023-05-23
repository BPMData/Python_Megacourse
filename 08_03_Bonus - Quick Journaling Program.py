# https://www.udemy.com/course/the-python-mega-course/learn/lecture/34597730#overview
# Quick daily journaling program

import os

directory = "./Day8Journals"

if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created.")
else:
    print("Directory already exists.")

# Check if the file ./Day8Journals/Journal01.txt exists
if not os.path.isfile("./Day8Journals/Journal01.txt"):
    # If it does not exist, create it with open
    open("./Day8Journals/Journal01.txt", "w")
    print("File ./Day8Journals/Journal01.txt created.")
else:
    # If it does exist, do nothing
    print("File ./Day8Journals/Journal01.txt already exists.")

date = input("Enter today's date in the format mm.dd.yyyy\n For example, 05.23.2023 for May 23, 2023: ")

mood = input("Rate your mood on a scale from 1, worst, to 10, best.")

thoughts = input("Write some thoughts about today:\n")

with open(f"./Day8Journals/{date}.txt", "w") as journalfile:
    journalfile.write(f"Today's mood was {mood} out of 10." + 2*"\n")
    journalfile.write(f"My thoughts for today were:\n{thoughts}")


