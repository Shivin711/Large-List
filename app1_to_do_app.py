from app1_functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is" , now)

while True:

    action = input("Type add, show, edit, complete, or exit: ")
    action = action.strip()

    if action.startswith("add"):

        todo = action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)
    
    elif action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif action.startswith("edit"):

        try:
            number = int(action[5:])
            number = number - 1

            todos = get_todos()

            new = input("Enter new todo: ")
            todos[number] = new + '\n'

            write_todos(todos)

        except ValueError:
            print("Invalid input. Please enter the number of the item you want to edit after you type 'edit'.")
            continue

    elif action.startswith("complete"):
        
        try:

            number = int(action[9:])

            todos = get_todos()

            index = number - 1
            remove = todos[index].strip("\n")
            todos.pop(number - 1)

            write_todos(todos)

            message = f"Todo '{remove}' was removed from the list."
            print(message)
        
        except IndexError:

            print("There aren't that many items in your todo list. Please try again.")
            continue

    elif action.startswith("exit"):
        break
    else:
        print("Invalid input. Please try again.")

print("Bye!")