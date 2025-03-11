#from todo_functions import get_todos, write_todos
import functions
import time

print(time.strftime("%b %d, %Y"))
while True:
    user_action = input("Enter add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    #match user_action:
    #    case 'add':
    #if 'add' in user_action:
    if user_action.startswith('add'):
            #todo = input("Enter to do: ") + "\n"
            
            todo = user_action[4:] + "\n"

            # file = open('todo.txt','r')
            # todo_list = file.readlines()add
            # file.close()

            
            todo_list = functions.get_todos()    


            todo_list.append(todo)

            #file = open('todo.txt','w')
            #file.writelines(todo_list)
            #file.close()


            
            functions.write_todos(todo_list)
            
         
    #    case 'show':
    elif user_action.startswith('show'):  

            todo_list = functions.get_todos()

            # new_todolist = [item.strip('\n') for item in todo_list]
            
            for i, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{i+1}-{item}"
                print(row)

            
    #    case 'edit':
    elif user_action.startswith('edit'):
            try:
            
                #number = int(input("Please enter number of todo to edit: "))
                number = int(user_action[5:])
                number = number-1

                todo_list = functions.get_todos()

                new_todo = input("Enter new value: ")

                todo_list[number] = new_todo + '\n'

                functions.write_todos(todo_list)

            except ValueError:
                  print("Your command is not valid")
                  continue

        
    #    case 'remove':
    elif user_action.startswith('remove'):
            try:
                #number = int(input("Please enter number of todo to edit: "))
                number = int(user_action[6:])
                
                todo_list = functions.get_todos()

                todo_list.pop(number-1)

                functions.write_todos(todo_list)

            except IndexError:
                  print("Your command is not valid")
                  continue

    #    case 'exit':
    elif user_action.startswith('exit'):  
            break
    #    case _:
    else:
            print("Please enter valid value")

print("Bye !!!")