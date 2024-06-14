# Main file for app1
# from functions import get_todos, write_todos
import functions
import time

while True:
    # print("Here's your list: ")
    # new_todos = [item.strip('\n') for item in todos]
    #
    # for index, item in enumerate(new_todos):
    #     print(f"{index + 1}. {item}")

    print(time.strftime("%b %d, %Y %H:%M:%S"))

    user_action = input("Type save, add, view, edit, complete, or exit: ")

    if user_action.startswith('add'):
        # list slicing operation, as a range, from x : to y
        todo = user_action[4:]
        # todo = input("Enter a To-Do Item: ") + "\n"
        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos, )

        print(f"{todo} was added!")

    elif user_action.startswith('view'):
        print("Here's your list: ")
        todos = functions.get_todos()
        # METHOD 1: remove formatting via for loop and strip function
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # METHOD 2: list comprehension [do action for each iteration]
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        todos = functions.get_todos()
        try:
            number = int(user_action[5:])

            # for index, item in enumerate(todos):
            #     item = item.strip('\n')
            #     print(f"{index + 1}. {item}")

            # number = int(input("Enter the Item Number: "))
            print(f"You selected: {str(number)}. {todos[int(number - 1)]}")
            new_todo = input("Enter revision: ") + "\n"
            todos[number - 1] = new_todo

            functions.write_todos(todos, )

            print("Update complete!", todos)
        except ValueError:
            print("Your command was not recognized. ")
            continue

    elif user_action.startswith('complete'):
        todos = functions.get_todos()
        try:
            number = int(user_action[9:])
            # for index, item in enumerate(todos):
            #     item = item.strip('\n')
            #     print(f"{index + 1}. {item}")
            # number = int(input("Enter the Item Number you Completed: "))

            index = number - 1
            todo_last_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, )

            print(f"Removed '{todo_last_remove}'. Nice job!")
        except IndexError:
            print("There is no item in that range. ")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not detected. Please try again. ")
print("Bye!")
 