
import os

import requests
import json
import re

from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository

class GenerativeAiResponseProcessingUtility:
    @staticmethod
    def extract_python_ortools_code_execution_value_errors(response_payload: str):
        # print('---- DEBUGGING ----', response_payload)
        results = re.findall(r"ValueError\(.*\)", response_payload)
        # print('---- DEBUGGING ----', results)
        number_results = len(results)
        python_ortools_code_execution_value_errors = []
        if (number_results > 0):
            python_ortools_code_execution_value_errors = results
        # print('---- DEBUGGING ----', '-------- BEGIN --------')
        # print('---- DEBUGGING ----', python_ortools_code_execution_value_errors)
        # print('---- DEBUGGING ----', '-------- END --------')
        return python_ortools_code_execution_value_errors
    @staticmethod
    def extract_python_ortools_code_execution_attribute_errors(response_payload: str):
        # print('---- DEBUGGING ----', response_payload)
        results = re.findall(r"AttributeError:.*", response_payload)
        # print('---- DEBUGGING ----', results)
        number_results = len(results)
        python_ortools_code_execution_attribute_errors = []
        if (number_results > 0):
            python_ortools_code_execution_attribute_errors = results
        # print('---- DEBUGGING ----', '-------- BEGIN --------')
        # print('---- DEBUGGING ----', python_ortools_code_execution_attribute_errors)
        # print('---- DEBUGGING ----', '-------- END --------')
        return python_ortools_code_execution_attribute_errors
    @staticmethod
    def extract_python_ortools_code_execution_errors(response_payload: str):
        python_ortools_code_execution_errors = []
        python_ortools_code_execution_value_errors = GenerativeAiResponseProcessingUtility.extract_python_ortools_code_execution_value_errors(response_payload)
        if (len(python_ortools_code_execution_value_errors) > 0):
            python_ortools_code_execution_errors.append(python_ortools_code_execution_value_errors)
        python_ortools_code_execution_attribute_errors = GenerativeAiResponseProcessingUtility.extract_python_ortools_code_execution_attribute_errors(response_payload)
        if (len(python_ortools_code_execution_attribute_errors) > 0):
            python_ortools_code_execution_errors.append(python_ortools_code_execution_attribute_errors)
        return python_ortools_code_execution_errors

    @staticmethod
    def extract_generated_python_code(response_payload: str, index_code_block_found: int = 0) -> str:
        return GenerativeAiResponseProcessingUtility.extract_generated_python_code_triple_back_quoted(response_payload, index_code_block_found)

    @staticmethod
    def extract_generated_python_code_triple_back_quoted(response_payload: str, index_code_block_found: int = 0):
        results = GenerativeAiResponseProcessingUtility.extract_generated_python_code_blocks_triple_back_quoted(response_payload)
        # print('---- DEBUGGING ----', results)
        number_results = len(results)
        code_block_found = ''
        if (number_results > index_code_block_found):
            code_block_found = results[index_code_block_found]
        if not code_block_found:
            return {
                'status': False,
                'code_block': ''
            }
        # print('---- DEBUGGING ----', '-------- BEGIN --------')
        # print('---- DEBUGGING ----', code_block_found)
        # print('---- DEBUGGING ----', '-------- END --------')
        extracted = {
            'status': True,
            'code_block': code_block_found
        }
        return extracted

    @staticmethod
    def extract_generated_python_code_blocks_triple_back_quoted(response_payload: str):
        # print('---- DEBUGGING ----', response_payload)
        results = re.findall(r'```python\s*([\s\S]*?)```', response_payload)
        # print('---- DEBUGGING ----', results)
        number_results = len(results)
        code_blocks_found = []
        if (number_results > 0):
            code_blocks_found = results
        # print('---- DEBUGGING ----', '-------- BEGIN --------')
        # print('---- DEBUGGING ----', code_blocks_found)
        # print('---- DEBUGGING ----', '-------- END --------')
        return code_blocks_found

    @staticmethod
    def extract_objective(code_execution_output_text: str, objective_prefix: str, make_lower_before_matching: bool = True) -> float:
        """
        """
        # First check if model is infeasible
        if "Model is infeasible" in code_execution_output_text:
            return None
        if make_lower_before_matching:
            objective_prefix = objective_prefix.lower()
            code_execution_output_text = code_execution_output_text.lower()
        # ---- Try to find objective score
        # ---- NOTE-ALTERNATIVE ---- match = re.search(rf'{objective_prefix}\s*([\d.e+-]+)', code_execution_output_text)
        match = re.search(rf'{objective_prefix}\s*([+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)', code_execution_output_text)
        # print('---- DEBUGGING-match ----', match)
        # ---- if not match:
        # ----     # If not found, try to find Optimal objective
        # ----     match = re.search(r'Optimal objective\s+([\d.e+-]+)', code_execution_output_text)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                return None
        return None

    @staticmethod
    def extract_objective_absolute(code_execution_output_text: str, make_lower_before_matching: bool = True) -> float:
        """
        """
        objective_prefix: str = 'OBJECTIVE='
        return GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix)

def main_test_extract_python_ortools_code_execution_value_error():
    python_ortools_code_execution_result = 'raise ValueError(\'Operators "<" and ">" not supported with the linear solver\')sdsd'
    response_payload = GenerativeAiResponseProcessingUtility.extract_python_ortools_code_execution_errors(
        python_ortools_code_execution_result)
    print(response_payload)

def main_test_extract_generated_python_code():
    response = 'asdasfda asdfasdf```python\nimport ortools.sat as sat\nfrom ortools import sat_solver\nfrom ortools.sat.python import cp_model\n\ndef solve_farm_problem(L, F1, P1, S1, F2, P2, S2):\n    # Create a new solver\n    model = cp_model.CpModel()\n\n    # Define the variables\n    x1 = model.NewIntVar(0, L, \'x1\')  # area of land planted with wheat\n    x2 = model.NewIntVar(0, L, \'x2\')  # area of land planted with barley\n\n    # Define the objective function (maximize profit)\n    obj_func = -model.NewCost(x1 * S1 + x2 * S2)  # Negative because we are maximizing\n    model.Minimize(obj_func)\n\n    # Define the constraints\n    # Fertilizer constraint\n    fertilizer_constraint = model.Add(F1*x1 + F2*x2 <= F)\n    # Pesticide constraint\n    pesticide_constraint = model.Add(P1*x1 + P2*x2 <= P)\n    # Area constraint (total area is L hectares)\n    area_constraint = model.Add(x1 + x2 == L)\n\n    # Add the solver and print results\n    solver = sat_solver.SATSolver()\n    status = solver.Solve(model)\n    if status == sat_solver.SATSOLVED:\n        print(f"Solution found: x1={int(x1.Value())}, x2={int(x2.Value())}")\n        return int(x1.Value()), int(x2.Value())\n    else:\n        print("No solution found")\n        return None, None\n\n# Example usage\nL = 1000  # total area in hectares\nF = 1000  # amount of fertilizer available (in kilograms)\nP = 2000  # amount of pesticide available (in kilograms)\n\nS1 = 500  # price of wheat per hectare (in dollars)\nS2 = 300  # price of barley per hectare (in dollars)\n\nx1, x2 = solve_farm_problem(L, F1, P1, S1, F2, P2, S2)\n```sdsd sdsf '
    response_payload = GenerativeAiResponseProcessingUtility.extract_generated_python_code(
        response)
    print(response_payload)

def main_test_extract_objective_case_0():
    code_execution_output_text = 'load c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\zlib1.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\abseil_dll.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\utf8_validity.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\re2.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\libprotobuf.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\highs.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\ortools.dll...\r\nSolution:\r\nArea planted with wheat (x1): 100.0\r\nArea planted with barley (x2): 0.0\r\nMaximum Profit: 20000.0\r\n'
    code_execution_output_text_result = GenerativeAiResponseProcessingUtility.extract_objective(
        code_execution_output_text,
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print(code_execution_output_text_result)

def main_test_extract_objective_case_1():
    code_execution_output_text = 'load c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\zlib1.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\abseil_dll.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\utf8_validity.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\re2.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\libprotobuf.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\highs.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\ortools.dll...\r\nSolution:\r\nOptimal area for wheat (x1): 100.0\r\nOptimal area for barley (x2): 1.4210854715202004e-14\r\nMaximum profit: 20000.000000000004\r\n'
    code_execution_output_text_result = GenerativeAiResponseProcessingUtility.extract_objective(
        code_execution_output_text,
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print(code_execution_output_text_result)

def main_test_extract_objective_case_2_cannot_extract_if_prompt_not_same_case():
    code_execution_output_text = 'load c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\zlib1.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\abseil_dll.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\utf8_validity.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\re2.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\libprotobuf.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\highs.dll...\r\nload c:\\git\\or_llm_cot_rl_agent\\.venv\\Lib\\site-packages\\ortools\\.libs\\ortools.dll...\r\nSolution:\r\nOptimal area for wheat (x1): 100.0\r\nOptimal area for barley (x2): 1.4210854715202004e-14\r\nMaximum profit: 20000.000000000004\r\n'
    code_execution_output_text_result = GenerativeAiResponseProcessingUtility.extract_objective(
        code_execution_output_text,
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit,
        False)
    print(code_execution_output_text_result)

if __name__ == "__main__":
    # main_test_extract_python_ortools_code_execution_value_error()
    main_test_extract_objective_case_0()
    main_test_extract_objective_case_1()
    main_test_extract_objective_case_2_cannot_extract_if_prompt_not_same_case()
    # main_test_extract_generated_python_code()
