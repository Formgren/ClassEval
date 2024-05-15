import json
from radon.visitors import ComplexityVisitor    


# Load the JSON file
with open('GPT_3_5_all.json', 'r') as f:
    data = json.load(f)

# Iterate over each task
for i in range(100):
    task_key = f"ClassEval_{i}"
    if task_key in data:
        task = data[task_key]
        predict_program = task.get('predict', '')

        # Calculate cyclomatic complexity
        visitor = FunctionVisitor.from_code(predict_program)
        complexity = cc_visit(predict_program)

        print(f"Cyclomatic complexity of program in {task_key}: {complexity}")