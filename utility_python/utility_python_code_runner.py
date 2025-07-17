
import asyncio
import os
import json
import re
import subprocess
import sys
import tempfile

class PythonCodeRunnerUtility:
    @staticmethod
    async def async_run_python_code(python_code: str, to_delete_python_code: bool = True, python_code_permanent_file_path: str = '', python_code_output_directory: str = '.', python_code_temp_file_name_prefix: str = 'g_'):
        try:
            if not python_code_permanent_file_path:
                with tempfile.NamedTemporaryFile(
                    mode="w",
                    suffix=".py",
                    prefix=python_code_temp_file_name_prefix,
                    dir=python_code_output_directory,
                    delete=False) as temp_file:
                    temp_file.write(python_code)
                    python_code_output_file_path = temp_file.name
            else:
                python_code_output_file_path = python_code_permanent_file_path
                with open(python_code_output_file_path, "w") as file:
                    file.write(python_code)
            proc = await asyncio.create_subprocess_exec(
                sys.executable,
                python_code_output_file_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await proc.communicate()

            if proc.returncode == 0:
                # print('---- DEBUGGING ---- Python code executed succssfully:\n')
                stdout_decoded = stdout.decode()
                # print(f'---- DEBUGGING ---- stdout_decoded: {stdout_decoded}')
                
                # best_obj = extract_best_objective(stdout_str)
                # if best_obj is not None:
                #     print(f"\n最优解值 (Best objective): {best_obj}")
                # else:
                #     print("\n未找到最优解值")
                # return True, str(best_obj)
                return {
                    'status': True,
                    'code': python_code,
                    'message': stdout_decoded
                }
            else:
                stderr_decoded = stderr.decode()
                print(f'---- DEBUGGING ---- Python code executed failed: {stderr_decoded}\n')
                return {
                    'status': False,
                    'code': python_code,
                    'message': stderr_decoded
                }
        except Exception as exception:
            print(f'---- DEBUGGING ---- Python code executed failed, exception: {exception}\n')
            return {
                'status': False,
                'code': python_code,
                'message': str(exception)
            }
        finally:
            if to_delete_python_code:
                print(f'---- DEBUGGING ---- deleting code file: {python_code_output_file_path}\n')
                if 'python_code_output_file_path' in locals() and os.path.exists(python_code_output_file_path):
                    os.remove(python_code_output_file_path)
            else:
                print(f'---- DEBUGGING ---- NOT deleting code file: {python_code_output_file_path}\n')
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ---- return {
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'status': True,
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'code': python_code,
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'message': 'Success'
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ---- }

async def async_main_test_run_python_code_happy_path():
    response_python_code = "from ortools.linear_solver import pywraplp\n\ndef maximize_profit(L, F, P, F1, P1, S1, F2, P2, S2):\n    # Create the linear solver with the SCIP backend\n    solver = pywraplp.Solver.CreateSolver('SCIP')\n    \n    # Variables\n    x1 = solver.NumVar(0, solver.infinity(), 'x1')  # hectares of wheat\n    x2 = solver.NumVar(0, solver.infinity(), 'x2')  # hectares of barley\n\n    # Constraints\n    solver.Add(x1 + x2 <= L)  # Land constraint\n    solver.Add(F1 * x1 + F2 * x2 <= F)  # Fertilizer constraint\n    solver.Add(P1 * x1 + P2 * x2 <= P)  # Pesticide constraint\n\n    # Objective function\n    solver.Maximize(S1 * x1 + S2 * x2)\n\n    # Solve the problem\n    status = solver.Solve()\n\n    # Check the result\n    if status == pywraplp.Solver.OPTIMAL:\n        print('Solution:')\n        print(f'Wheat (x1) hectares = {x1.solution_value()}')\n        print(f'Barley (x2) hectares = {x2.solution_value()}')\n        print(f'Maximized profit = {solver.Objective().Value()}')\n    else:\n        print('The problem does not have an optimal solution.')\n\n# Example values\nL = 100  # Total land in hectares\nF = 500  # Total fertilizer in kilograms\nP = 300  # Total pesticide in kilograms\nF1 = 5   # Fertilizer required per hectare of wheat\nP1 = 2   # Pesticide required per hectare of wheat\nS1 = 100 # Selling price per hectare of wheat\nF2 = 4   # Fertilizer required per hectare of barley\nP2 = 3   # Pesticide required per hectare of barley\nS2 = 150 # Selling price per hectare of barley\n\nmaximize_profit(L, F, P, F1, P1, S1, F2, P2, S2)\n"
    execution_result = await PythonCodeRunnerUtility.async_run_python_code(response_python_code)
    print(f'---- DEBUGGING ---- async_main_test_run_python_code_happy_path(), execution_result: {execution_result}')

if __name__ == "__main__":
    asyncio.run(async_main_test_run_python_code_happy_path())