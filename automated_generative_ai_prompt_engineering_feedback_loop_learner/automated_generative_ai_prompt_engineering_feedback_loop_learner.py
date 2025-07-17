
import asyncio
import os
import base64
import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from utility_openai.utility_openai_azure_foundry import OpenaiAzureFoundryUtility
from utility_problem_sets.problem_sets_utility import ProblemSetsUtility
from utility_prompt_engineering.prompt_generator import Prompt
from utility_prompt_engineering.prompt_generator import Prompts
from utility_prompt_engineering.prompt_generator import PromptGenerator
from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository
from utility_prompt_engineering.prompt_operations_research_phrases import PromptOperationsResearchPhrases
from utility_python.utility_python_code_runner import PythonCodeRunnerUtility
from utility_response_processor.utility_generative_ai_response_processor import GenerativeAiResponseProcessingUtility
from utility_response_processor.utility_generative_ai_response_processor_for_fisher_optimization_problem import GenerativeAiResponseProcessingForFisherOptimizationProblemUtility

class AutomatedGenerativeAiPromptEngineeringFeedbackLoopLearner:
    @staticmethod
    async def automated_generative_ai_feedback_loop_learner(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        question: str,
        answer: float,
        to_delete_python_code: bool,
        python_code_permanent_file_path_prefix: str,
        number_loop_iterations: int = 8,
        python_code_permanent_file_path_extension_for_illegal_program: str = '_illegal_program',
        python_code_permanent_file_path_extension_for_runnable_program: str = '_runnable_program',
        python_code_permanent_file_path_extension: str = '.py'):
        # ---- NOTE-FOR-REFERENCE ---- to_delete_python_code: bool = False
        # ---- NOTE-FOR-REFERENCE ---- generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
        # ---- NOTE-FOR-REFERENCE ---- generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
        # ---- NOTE-FOR-REFERENCE ---- bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
        # ---- NOTE-FOR-REFERENCE ---- generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
        # ---- NOTE-FOR-REFERENCE ---- file_path_to_problem_sets: str = os.path.join('problem_sets', 'lpwp_combined_result.json')
        # ---- NOTE-FOR-REFERENCE ---- problem_sets = ProblemSetsUtility.load_problem_sets(file_path_to_problem_sets)
        # ---- NOTE-FOR-REFERENCE ---- problem_0_question = problem_sets['0']['question']
        # ---- NOTE-FOR-REFERENCE ---- problem_0_answer = problem_sets['0']['answer']
        # ---- NOTE-FOR-REFERENCE ---- print('---- DEBUGGING-problem_0_question ----', problem_0_question)
        # ---- NOTE-FOR-REFERENCE ---- print('---- DEBUGGING-problem_0_answer ----', problem_0_answer)
        prompts = []
        PromptGenerator.add_system_prompt(prompts, PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddonWithMixedIntegerProgramSpecific)
        PromptGenerator.add_user_prompt(prompts, question)
        PromptGenerator.add_user_prompt(prompts, PromptOperationsResearchExampleRepository.FisheryOptimizationProblemOptimizationProblemSpecifics)
        for looping_index in range(number_loop_iterations):
            print('---- DEBUGGING-looping_index ----', looping_index)
            print(f'---- {looping_index}-DEBUGGING-prompts ----', prompts)
            generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt_using_multiple_prompts(
                generative_ai_client,
                generative_model_configuration,
                generative_model_parameters,
                prompts)
            response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
            print(f'---- {looping_index}-DEBUGGING-response_payload ----', response_payload)
            code_block = response_payload['code_block']
            python_code_permanent_file_path = f'{python_code_permanent_file_path_prefix}_{looping_index}{python_code_permanent_file_path_extension}'
            print(f'---- {looping_index}-DEBUGGING-python_code_permanent_file_path ----', python_code_permanent_file_path)
            code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block, to_delete_python_code, python_code_permanent_file_path)
            print(f'---- {looping_index}-DEBUGGING-code_block_execution_result ----', code_block_execution_result)
            code_block_execution_result_message = code_block_execution_result['message']
            print(f'---- {looping_index}-DEBUGGING-code_block_execution_result_message ----', code_block_execution_result_message)
            code_block_execution_result_message_value_error_detection = GenerativeAiResponseProcessingUtility.extract_python_ortools_code_execution_errors(
                code_block_execution_result_message)
            print(f'---- {looping_index}-DEBUGGING-code_block_execution_result_message_value_error_detection ----', code_block_execution_result_message_value_error_detection)
            has_errors: bool = len(code_block_execution_result_message_value_error_detection) > 0
            print(f'---- {looping_index}-DEBUGGING-has_errors ----', has_errors)
            if not has_errors:
                code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective_absolute(
                    code_block_execution_result_message,
                    PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
                print(f'---- {looping_index}-DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)
                prompt_for_objective_improvement: str = f'{PromptOperationsResearchPhrases.PleaseImporveTheGeneratedCodeWithBetterSolutionWithHigherObjectiveScore} than {code_block_execution_result_objective}.'
                print(f'---- {looping_index}-DEBUGGING-prompt_for_objective_improvement ----', prompt_for_objective_improvement)
                python_code_permanent_file_path_runnable_program: str = f'{python_code_permanent_file_path_prefix}_{looping_index}_{python_code_permanent_file_path_extension_for_runnable_program}{python_code_permanent_file_path_extension}'
                print(f'---- {looping_index}-DEBUGGING-python_code_permanent_file_path_runnable_program ----', python_code_permanent_file_path_runnable_program)
                if not to_delete_python_code:
                    os.rename(python_code_permanent_file_path, python_code_permanent_file_path_runnable_program)
            else:
                code_block_execution_result_message_value_error: str = code_block_execution_result_message_value_error_detection[0]
                prompt_for_error_correction: str = f'{PromptOperationsResearchPhrases.PleaseExamineTheGeneratedCodeAndFixAnyBuildErrors}: {code_block_execution_result_message_value_error}'
                print(f'---- {looping_index}-DEBUGGING-prompt_for_error_correction ----', prompt_for_error_correction)
                prompts_with_prompt_for_error_correction = PromptGenerator.add_user_prompt(prompts, prompt_for_error_correction)
                print(f'---- {looping_index}-DEBUGGING-prompts_with_prompt_for_error_correction ----', prompts_with_prompt_for_error_correction)
                python_code_permanent_file_path_illegal_program: str = f'{python_code_permanent_file_path_prefix}_{looping_index}_{python_code_permanent_file_path_extension_for_illegal_program}{python_code_permanent_file_path_extension}'
                print(f'---- {looping_index}-DEBUGGING-python_code_permanent_file_path_illegal_program ----', python_code_permanent_file_path_illegal_program)
                if not to_delete_python_code:
                    os.rename(python_code_permanent_file_path, python_code_permanent_file_path_illegal_program)

async def main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem_in_automated_generative_ai_feedback_loop_learner():
    to_delete_python_code: bool = False
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    file_path_to_problem_sets: str = os.path.join('problem_sets', 'lpwp_combined_result.json')
    problem_sets = ProblemSetsUtility.load_problem_sets(file_path_to_problem_sets)
    problem_0_question = problem_sets['0']['question']
    problem_0_answer = problem_sets['0']['answer']
    await AutomatedGenerativeAiPromptEngineeringFeedbackLoopLearner.automated_generative_ai_feedback_loop_learner(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        problem_0_question,
        problem_0_answer,
        to_delete_python_code,
        'generated_automated_generative_ai_feedback_loop_using_gpt_4o_azure_foundry_FisheryOptimization_try')

if __name__ == "__main__":
    asyncio.run(main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem_in_automated_generative_ai_feedback_loop_learner())
