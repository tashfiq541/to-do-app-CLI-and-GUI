import PySimpleGUI as sg
from functions import get_todos, write_todos
import datetime

time = datetime.datetime.now()

sg.theme("Black")
layout = [
    [sg.Text("", key='clock')],
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter to-do", key="todo"), sg.Button("Add")],
    [sg.Listbox(get_todos(), key="todos", enable_events=True,
                size=(45, 10)), sg.Button("Edit"), sg.Button("Completed")]
]

window = sg.Window("My To-Do App", layout, font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y  %I:%M %p"))
    if event == 'Add':
        todos = get_todos()
        todos.append(values['todo'] + '\n')
        write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value="")

    elif event == 'Edit':
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item", font=("Helvetica", 20))

    elif event == "Completed":
        try:
            todo_to_completed = values['todos'][0]
            todos = get_todos()
            index = todos.index(todo_to_completed)
            todos.pop(index)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        except IndexError:
            sg.popup("Please select an item", font=("Helvetica", 20))

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == sg.WIN_CLOSED:
        break

window.close()
