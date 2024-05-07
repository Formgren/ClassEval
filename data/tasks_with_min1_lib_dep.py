import json

# Load the data from the JSON file
with open('ClassEval_data.json') as f:
    data = json.load(f)

# Filter out tasks that have at least one method with a library dependency
tasks_with_lib_dependencies = [task for task in data if any(method['dependencies']['lib_dependencies'] for method in task['methods_info'])]

# Write the tasks with library dependencies to a new JSON file
with open('tasks_with_lib_dependencies.json', 'w') as f:
    json.dump(tasks_with_lib_dependencies, f, indent=4)

# Print the task id and the names of the methods that have library dependencies for each task
counter = 0
for task in tasks_with_lib_dependencies:
    print(f"Task ID: {task['task_id']}")
    counter += 1
    for method in task['methods_info']:
        if method['dependencies']['lib_dependencies']:
            print(f"Method with library dependencies: {method['method_name']}")
    print(counter)