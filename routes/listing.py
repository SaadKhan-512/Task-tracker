import json

def list_everything():
    with open("data.json", "r") as file:
            tasks = json.load(file)

    for  task in tasks:
        print(f"Task_id : {task["id"]}")
        print(f"Description : {task["description"]}")
        print(f"Status : {task["status"]}")
        print(f"Created_At : {task["created_At"]}")
        print(f"Updated_At : {task["updated_At"]}")
        print()

def list_done():
    with open("data.json", "r") as file:
            tasks = json.load(file)
    
    for  task in tasks:
        if(task["status"] == "done"):
            print(f"Task_id : {task["id"]}")
            print(f"Description : {task["description"]}")
            print(f"Status : {task["status"]}")
            print(f"Created_At : {task["created_At"]}")
            print(f"Updated_At : {task["updated_At"]}")
            print()

def list_in_progress():

    with open("data.json", "r") as file:
            tasks = json.load(file)
    
    
    for  task in tasks:
            if(task["status"] == "in-progress"):
                print(f"Task_id : {task["id"]}")
                print(f"Description : {task["description"]}")
                print(f"Status : {task["status"]}")
                print(f"Created_At : {task["created_At"]}")
                print(f"Updated_At : {task["updated_At"]}")
                print()

def list_todo():

    with open("data.json", "r") as file:
            tasks = json.load(file)
    
    
    for  task in tasks:
            if(task["status"] == "todo"):
                print(f"Task_id : {task["id"]}")
                print(f"Description : {task["description"]}")
                print(f"Status : {task["status"]}")
                print(f"Created_At : {task["created_At"]}")
                print(f"Updated_At : {task["updated_At"]}")
                print()