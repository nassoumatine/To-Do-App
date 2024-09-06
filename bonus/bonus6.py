#This file will create files in filenames
#Each file will contain the content in contents respectively

contents = ["All carrots are to be sliced"
            "longitudinally",
            "The carrots were reported sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    print(content, filename)
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()


a = "I am a string " \
    "on my own"
