filenames = ["reqs.txt", "report.txt", "results.txt"]

contents = ["All carrots must be sliced in that Japanese method I forget what it's called but it's nice.",
            "All the carrots were sliced up fancy-like",
            "Carrot slicer sliced the carrots well."]

for content,filename in zip(contents,filenames):
    file = open(f"TestDir/{filename}","w")
    file.write(content)
    file.close()