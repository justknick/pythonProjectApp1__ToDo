filenames = ['s8b-1.doc', 's8b-1.report', 's8b-1.presentation']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)