# On the side panel there's a s7e1-bear.txt file. The existing code opens that
# file in read mode.
# Below that code, please read the file content and print out the content.

filename = open('../files/s7e1-bear.txt', 'r')
content = filename.readlines()
filename.close()
print(content[0])
