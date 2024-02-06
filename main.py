from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action == 'add':
        todo = input("Enter a todo: ") + "\n"
        todos = get_todos("todos.txt")
        todos.append(todo)
        write_todos("todos.txt", todos)

    elif user_action == 'show':
        todos = get_todos("todos.txt")
        for index,  item in enumerate(todos):
            print(f"{index + 1} - {item.strip().title()}")

    elif user_action == 'edit':
        number = int(input("Number of the todo to edit: "))
        new_todo = input("Enter new todo: ")
        todos = get_todos("todos.txt")
        todos[number - 1] = new_todo + '\n'
        write_todos("todos.txt", todos)

    elif user_action == 'complete':
        number = int(input("Number of the todo to complete: "))
        todos = get_todos("todos.txt")
        print(f"Todo {todos[number - 1].strip()} has been removed from the list")
        todos.pop(number - 1)
        write_todos("todos.txt", todos)

    else:
        break
print('Bye!')