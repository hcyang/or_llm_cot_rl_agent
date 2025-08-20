
import asyncio
import os
import json
import re
import subprocess
import sys
import tempfile

from utility_debugging.utility_debugging import DebuggingUtility

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
                # DebuggingUtility.debug('---- DEBUGGING ---- Python code executed succssfully:\n')
                stdout_decoded = stdout.decode()
                # DebuggingUtility.debug(f'---- DEBUGGING ---- stdout_decoded: {stdout_decoded}')
                
                # best_obj = extract_best_objective(stdout_str)
                # if best_obj is not None:
                #     DebuggingUtility.info(f"\n最优解值 (Best objective): {best_obj}")
                # else:
                #     DebuggingUtility.info("\n未找到最优解值")
                # return True, str(best_obj)
                return {
                    'status': True,
                    'code': python_code,
                    'message': stdout_decoded
                }
            else:
                stderr_decoded = stderr.decode()
                DebuggingUtility.debug(f'---- DEBUGGING ---- Python code executed failed: {stderr_decoded}\n')
                return {
                    'status': False,
                    'code': python_code,
                    'message': stderr_decoded
                }
        except Exception as exception:
            DebuggingUtility.debug(f'---- DEBUGGING ---- Python code executed failed, exception: {exception}\n')
            return {
                'status': False,
                'code': python_code,
                'message': str(exception)
            }
        finally:
            if to_delete_python_code:
                DebuggingUtility.debug(f'---- DEBUGGING ---- deleting code file: {python_code_output_file_path}\n')
                if 'python_code_output_file_path' in locals() and os.path.exists(python_code_output_file_path):
                    os.remove(python_code_output_file_path)
            else:
                DebuggingUtility.debug(f'---- DEBUGGING ---- NOT deleting code file: {python_code_output_file_path}\n')
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ---- return {
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'status': True,
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'code': python_code,
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ----     'message': 'Success'
        # ---- NOTE-FALL-BACK-MAY-NOT-NEED ---- }

async def async_main_test_run_python_code_happy_path():
    response_python_code = "DebuggingUtility.info('Hello, World')\n"
    execution_result = await PythonCodeRunnerUtility.async_run_python_code(response_python_code)
    DebuggingUtility.debug(f'---- DEBUGGING ---- async_main_test_run_python_code_happy_path(), execution_result: {execution_result}')

if __name__ == "__main__":
    asyncio.run(async_main_test_run_python_code_happy_path())