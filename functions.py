# Custom Functions
FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Reads the text file and returns contents as a list. """
    # Open/read file, Get user input
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    # Return is a statement
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the new to-do item to the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    # return todos_arg


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
