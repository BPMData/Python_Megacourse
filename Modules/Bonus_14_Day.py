def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches # we can do better than this by creating a {dictionary}.
    return {"Feet": feet, "Inches": inches}


def convert(Feet, Inches):
    meters = Feet * 0.3048 + Inches * 0.0254
    return meters
