# Implement a function that gets a person's name (e.g. john) as
# a parameter and returns a greeting (e.g. Hi John). Note that
# the first letter of the person's name should always be uppercase.
name = 'lisa'

def get_name(name_local):
    message_local = f"Hi {name_local.capitalize()}"
    return message_local


print(get_name(name))