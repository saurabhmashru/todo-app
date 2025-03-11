def get_todos():
      with open('todo.txt','r') as file:
            todo_local_list = file.readlines()
      return todo_local_list

def write_todos(todo_list_arg):
      with open('todo.txt','w') as file:
        file.writelines(todo_list_arg)