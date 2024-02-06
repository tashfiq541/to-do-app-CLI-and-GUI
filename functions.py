FILENAMAE = "todos.txt"
def get_todos():
    with open(FILENAMAE, "r") as file:
        return file.readlines()


def write_todos(todos):
    with open(FILENAMAE, "w") as file:
        file.writelines(todos)