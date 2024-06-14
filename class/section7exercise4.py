# Use Python to create a file with name file.txt and
# write the text snail there.

contents = ['snail']
filenames = ['s7e4-file.txt']

for content, filename in zip(contents, filenames):
    document = open(f'files/{filename}', 'w')
    document.write(content)
