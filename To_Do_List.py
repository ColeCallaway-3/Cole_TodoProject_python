print("Welcome To Your Todo List")

To_List = []

while True:
    task = input("Add Today's Tasks (q to quit): ")
    if task == "q":
        break
    else:
        completion = input(f" Did you complete {task} today(Y or N)?")
        To_List.append(task)
print(" ------Here's Your To-do List------")

for task in To_List:
    print(task)
