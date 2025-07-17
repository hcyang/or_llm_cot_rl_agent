
import json
import os

class ProblemSetsUtility:
    @staticmethod
    def load_problem_sets(problem_sets_file_path: str) -> any:        
        # Open and read the JSON file
        with open(problem_sets_file_path, 'r') as file:
            loaded_json_object = json.load(file)
            return loaded_json_object
        return None

def main_test_happy_path_complexor():
    file_path_to_problem_sets: str = os.path.join('problem_sets', 'complexor_combined_result.json')
    problem_sets = ProblemSetsUtility.load_problem_sets(
        file_path_to_problem_sets)
    print(problem_sets)

def main_test_happy_path_lpwp():
    file_path_to_problem_sets: str = os.path.join('problem_sets', 'lpwp_combined_result.json')
    problem_sets = ProblemSetsUtility.load_problem_sets(
        file_path_to_problem_sets)
    print(problem_sets)

if __name__ == "__main__":
    # main_test_happy_path_complexor()
    main_test_happy_path_lpwp()
