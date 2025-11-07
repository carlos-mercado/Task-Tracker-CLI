import json
import sys

def remove(task_name, data):
    for i in range(0, len(data)):
        if(data[i]["name"] == task_name):
            #data.remove[{task_name : data[i][task_name]}]
            data.pop(i);
            with open("./tasks.json", "w") as file:
                json.dump(data, file, indent = 4)
            return;

    print("Could not find task.");

def add(name, status, data):
    data.append({"name" : name, "status" : status});
    pretty = json.dumps(data, indent = 4)
    print(pretty)
    with open("./tasks.json", "w") as file:
        json.dump(data, file, indent = 4)

def update(taskName, data, newStatus):
    for i in range(0, len(data)):
        if(data[i]["name"] == taskName):
            data[i]["status"] = newStatus;
            with open("./tasks.json", "w") as file:
                json.dump(data, file, indent = 4)
            return;
    print("Could not find task.");

def listTasks(data, mode):
    for i in range(0, len(data)):
        if(data[i]["status"] == mode):
            pretty = json.dumps(data[i], indent = 4)
            print(pretty)

try:
    with open('./tasks.json', 'x') as f:
        f.write('[\n]');
        print("file successfully created")
except FileExistsError: 
    print("file already exists... continuing")

while(True):
    #load the file


    with open('./tasks.json', 'r') as file:
            data = json.load(file)

    name = input("Add (1), Update (2), Delete (3), Print(4), Quit(Q)\n")

    match name:
        case '1':
            task_name = input("Task name: ")
            status = input("Status (in progress, done, not done): ")
            add(task_name, status, data)
        case '2':
            task_name = input("Task name: ")
            updated_status = input("Status: ")
            update(task_name, data, updated_status);
        case '3':
            task_name = input("Task name: ")
            remove(task_name, data)
        case '4':
            mode = input("Tasks to print (done, not done, in progress): ")
            listTasks(data, mode)
        case _:
            print("Quitting...")
            sys.exit(0);
