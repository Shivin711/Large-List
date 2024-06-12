from app1_functions import get_todos, write_todos
import streamlit as st

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

todos = get_todos()
st.title("Large List:")
st.subheader("The perfect list creator.")

for index , todo in enumerate(todos):
    checkbox = st.checkbox(todo , key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="" , placeholder="Add a new item..." , on_change=add_todo , key="new_todo")