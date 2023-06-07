def get_average():
    with open("venv/testdata/11data","r") as file:
        tempdata = file.readlines()
    values = tempdata[1:]
    values = [float(i) for i in values]

    avg_local = sum(values)/len(values)
    return avg_local


average = get_average()

print(average)

