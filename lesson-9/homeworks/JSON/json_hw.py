import json
import csv

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def calculations(file_path):
    tasks = json.load(file_path)
    
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks)/total_tasks
    
    return total_tasks, completed_tasks, pending_tasks, avg_priority

def json_to_csv(json_file,csv_file):
    with open(json_file, 'r') as file1:
        tasks = json.load(file1)
        
    with open(csv_file, 'w', newline='') as file2:
        write = csv.writer(file2)
        write.writerow(['ID','Task Name','Completed Status','Priority'])
        
        for task in tasks:
            write.writerow([task['id'],task['task_name'],task['completed'],task['priority']])