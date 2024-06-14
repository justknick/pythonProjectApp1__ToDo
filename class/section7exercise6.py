# Open your computer IDE and place the following in a Python file:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# Then, create a program that:
# 1. generates multiple text files by iterating over the filenames list,
# 2. and writes the text Hello  inside each generated text file.
filenames = ['s7e6-doc.txt', 's7e6-report.txt', 's7e6-presentation.txt']
# file_number = len(filenames)
contents = []

for item in filenames:
    contents.append("Hello")

for content, filename in zip(contents, filenames):
    document = open(f'files/{filename}', 'w')
    document.writelines(content)
    document.close()
