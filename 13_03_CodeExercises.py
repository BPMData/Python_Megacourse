# Exercise 1
def get_age(year_of_birth, current_year = 2023):
    age = current_year - year_of_birth
    return age

print(get_age(1986))

# Exercise 2

def get_nr_items(list):
    splitlist = list.split(",")
    nr = len(splitlist)
    return nr

print(get_nr_items('apple,banana,orange'))


# Exercise 3
def squarea(length):

    side = int(length)
    area = side * side
    return area


print(squarea(9))

#Exercise 4
def tempeval(temp):
    temp = int(temp)

    if temp > 7:
        print("Warm")
    else:
        print("Cold")

tempeval(-7)

# or

def tempeval(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

# Exercise 5

def foo(string):
    if len(string) >= 8:
        return True
    else:
        return False

print(foo("78"))

# Bug fixing exercise:

def calculate_time(g=9.80665, h): # h has to go before g, default arguments go to the back of the function. 
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)