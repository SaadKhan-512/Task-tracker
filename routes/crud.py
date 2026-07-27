import json, random, uuid
from datetime import datetime

def add(data: str):
    with open("data.json", "r") as file:
        dt = json.load(file)

    task = {
        "id": uuid.uuid4().hex,
        "description": data,
        "status": "todo",
        "created_At": datetime.now().isoformat(),
        "updated_At": datetime.now().isoformat()
    }

    dt.append(task)

    with open("data.json", "w") as file:
        json.dump(dt, file, indent=4)

def update(id, data):
    with open("data.json", "r") as file:
        tasks = json.load(file)

    i = 0

    for t in tasks:
         if t["id"] == id:
            task = tasks[i]
            task["description"] = data
            task["updated_At"] = datetime.now().isoformat()

    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delete(id):
    with open("data.json", "r") as file:
            tasks = json.load(file)

    i = 0

    for task in tasks:
        if task["id"] == id:
            del tasks[i]
        i += 1
    
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Task with id of {id} has been deleted sucessfully.")

def mark_status(id, status):
    with open("data.json", "r") as file:
            tasks = json.load(file)

    for task in tasks:
        if task["id"] == id:
            task["status"] = status
        
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)