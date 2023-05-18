filenames = ["reqs.txt", "report.txt", "results.txt","I_Remembered.txt"]

contents = ["All carrots must be sliced in that Japanese method "
            "I forget what it's called but it's nice.", # Note this line and the one above it is one string.
            "All the carrots were sliced up fancy-like",
            "Carrot slicer sliced the carrots well.",
            "I rememembered, it's called Rangiri. Which literally means 'Chopping' in Japanese. \nWhich is dumb."
            "There's no way that's what it's actually called in Japan, is it?"]

for content,filename in zip(contents,filenames):
    file = open(f"TestDir/{filename}","w")
    file.write(content)
    file.close()

a = "I am a string on " \
    "my" \
    " own "

# Note that if it's a SINGLE string, you need these backslashes, but luckily PyCharm adds it for you.

# Bugs

# Bugs
# Solution 1:

file = open("TestDir/Data.txt", 'w')

file.write("100.12" + "\n")
file.write("111.23")
file.close()

file2 = open("TestDir/Data.txt","r")
content = file2.read()
print(content)

# Solution 2:
