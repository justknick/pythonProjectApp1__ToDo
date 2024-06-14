# Implement a function that gets a person's name as a parameter and
# greets the person with Hi Person. For example, if I call your
# function using foo("lisa") the function should return Hi lisa .
name = 'lisa'

def get_name(name_local):
    message_local = f"Hello {name_local}"
    return message_local


print(get_name(name))