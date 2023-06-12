# import glob
#
# myfiles = glob.glob("TestDir/*.txt")
#
# print(myfiles)
#
# for filepath in myfiles:
#     with open(filepath,"r") as file:
#         print(file.read())

# import csv
#
# with open("TestDir/weather.csv","r") as file:
#     data = list(csv.reader(file))
#
# print(data)
#
# print(type(data))
#
# city = input("Enter a city:")
#
# for row in data:
#     if row[0] == city:
#             print(row[1])

# import shutil
#
# shutil.make_archive("TestDir/output", "zip", "TestDir")

import webbrowser

user_term = input("Enter a search term: ").replace(" ","+")
webbrowser.open(f"https://www.google.com/search?q=" + user_term)