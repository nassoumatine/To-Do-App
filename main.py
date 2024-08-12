
todos = []

while True:
    user_action = input("type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}-{item}"
                print(row)
        case'edit':
            number = int(input("number od the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("number od the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break

print("Bye!")