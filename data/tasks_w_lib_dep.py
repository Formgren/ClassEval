import json

# Load the JSON data
with open('ClassEval_data.json') as f:
    data = json.load(f)

# Filter tasks with library dependencies
tasks_with_lib_dependencies = [task for task in data if any(method['dependencies']['lib_dependencies'] for method in task['methods_info'])]

# # Write tasks with library dependencies to a new JSON file
# with open('tasks_with_lib_dependencies.json', 'w') as f:
#     json.dump(tasks_with_lib_dependencies, f)

# Print tasks and their methods with library dependencies
for task in tasks_with_lib_dependencies:
    methods_with_lib_dependencies = [method['method_name'] for method in task['methods_info'] if method['dependencies']['lib_dependencies']]
    print(f"{task['task_id']}, {', '.join(methods_with_lib_dependencies)}")