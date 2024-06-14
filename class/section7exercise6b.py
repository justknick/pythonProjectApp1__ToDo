filenames = ['s7e6b-doc.txt', 's7e6b-report.txt', 's7e6b-presentation.txt']

for filename in filenames:
    document = open(f'files/{filename}', 'w')
    document.write("Hallo")
    document.close()