import json
import re

def extract_passed_programs(program_file, results_file, output_file):
    # Load the programs and the test file
    with open(program_file, 'r') as f:
        programs = json.load(f)
    with open(results_file, 'r') as f:
        results = json.load(f)

    # Extract the programs that passed all the tests
    i = 0
    passed_programs = []
    for task_id in results['GPT_3_5_iteration_2_new_prompt']:
        print(task_id)
        print(type(task_id))
        if results['GPT_3_5_iteration_2_new_prompt'][task_id]['TestClass']['class_success'] > 0:
            # strip the string of ClassEval_ and only taske the number
            task_number = int(re.search(r'\d+', task_id).group())
            passed_programs.append(programs[task_number])
            
        # print(programs[task_number]['predict'])
    with open(output_file, 'w') as f:
        json.dump(passed_programs, f)


file_path_programs = '/Users/mac/Desktop/KTH/TIDAB3/Exjobb/ClassEval/output/model_output/GPT_3_5_iteration_2_new_prompt.json'
file_path_results ='/Users/mac/Desktop/KTH/TIDAB3/Exjobb/ClassEval/output/result/detailed_result.json'
output_file = 'only_functional_programs.json'
extract_passed_programs(file_path_programs, file_path_results, output_file)