mylist = ["a","b","c","d"]

z = mylist
# z is type list


x = mylist[1]

# x is type str

# How to get the index number? If you know the exact item, you can try:

mylist.index("c")
# 2

# Edit a list with indeces

mylist.__setitem__(2,"OBAMA")

mylist
# [a, b, OBAMA, d]

# However, the preferred method is to use subsetting via []

mylist[2] = "JOESEPH R BIDEN"

mylist
# ['a', 'b', 'JOESEPH R BIDEN', 'd']

# TUPLES

filename = "1. Raw data.csv"

filename.replace(".","-")
# "1 - Raw data-csv"
filename
# "1. Raw data.csv" >>>> Clearly filename was not permanently altered by .replace()
filename_new = filename.replace(".","-")

filename_new
# "1 - Raw data-csv"

# Note that this DOES NOT work:

filename.replace(".","-") = filename_new
# Syntax error

# Permanently overwrite the string:

filename = filename.replace(".","-")
filename

# But we don't want to break our extension, soooo restart

filename = "1. Raw data.csv"
filename = filename.replace(".","-",1)
filename
# "1 - Raw data.csv"

# What if you want a list that can't be edited? Use a tuple!

filenames = "Cool Guy.wmv","Funny_Sounds.exe","Butter DOg"
type(filenames)
# Tuple

filenames = ["Cool Guy.wmv","Funny_Sounds.exe","Butter DOg"]
type(filenames)
#List

filenames = ("Cool Guy.wmv","Funny_Sounds.exe","Butter DOg")
type(filenames)
# Tuple again

print(filenames)

filenames[1]
#Funny_Sounds.exe

filenames[1] = "Obama_Speech.exe"
# Nope, error.