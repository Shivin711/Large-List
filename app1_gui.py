from app1_functions import get_todos, write_todos
import FreeSimpleGUI as sg
import time

sg.theme("Light Brown11")
clock = sg.Text("" , key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo:" , key="todo")

add = sg.Button("Add" , size=15)
edit = sg.Button("Edit")
complete = sg.Button("Complete")
exit = sg.Button("Exit")

list_box = sg.Listbox(values=get_todos() , key="todos" , 
                      enable_events=True , size=[45 , 10])

window = sg.Window("My To-Do App" ,
                    layout=[[clock , exit] ,
                            [label] ,
                            [input_box , add] ,
                            [list_box , edit , complete]] ,
                    font=("Times New Roman" , 20))

while True:

    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    if event == "Add":

        todos = get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        write_todos(todos)
        window["todos"].update(values=todos)

    if event == "Edit":

        try:

            todo_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        
        except IndexError:

            sg.popup("Please select an item to edit first." , font=("Times New Roman" , 20))

    if event == "Complete":
        
        try:

            todo_complete = values["todos"][0]
            todos = get_todos()
            todos.remove(todo_complete)
            write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        
        except IndexError:

            sg.popup("Please select an item to complete first." , font=("Times New Roman" , 20))

    if event == "Exit":
        break

    if event == "todos":        
        window["todo"].update(value=values["todos"][0])

    if event == sg.WIN_CLOSED:
        break

window.close()