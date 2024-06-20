contents = ['all carrots go to heaven.',
            'the carrots slice.',
            'no more carrots.']

filenames = ['s7b-doc.txt', 's7b-report.txt', 's7b-presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'files/{filename}', 'w')
    file.write(content)
