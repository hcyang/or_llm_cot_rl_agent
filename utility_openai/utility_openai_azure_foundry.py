
import asyncio
import os
import base64
import json
from openai import AzureOpenAI
from openai import AsyncAzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from utility_problem_sets.problem_sets_utility import ProblemSetsUtility
from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository
from utility_prompt_engineering.prompt_operations_research_phrases import PromptOperationsResearchPhrases
from utility_python.utility_python_code_runner import PythonCodeRunnerUtility
from utility_response_processor.utility_generative_ai_response_processor import GenerativeAiResponseProcessingUtility

class OpenaiAzureFoundryUtility:
    @staticmethod
    def get_generative_model_configuration(api_version):
        endpoint = os.getenv('ENDPOINT_URL')
        deployment = os.getenv('DEPLOYMENT_NAME')
        token_provider_endpoint = os.getenv('TOKEN_PROVIDER_ENDPOINT_URL')
        api_version = os.getenv('API_VERSION')
        generative_model_configuration = {
            'endpoint': endpoint,
            'deployment': deployment,
            'token_provider_endpoint': token_provider_endpoint,
            'api_version': api_version
        }
        return generative_model_configuration

    @staticmethod
    def get_generative_model_parameters():
        azure_openai_client_parameter_max_tokens=9600
        azure_openai_client_parameter_temperature=0.7
        azure_openai_client_parameter_top_p=0.95
        azure_openai_client_parameter_frequency_penalty=0
        azure_openai_client_parameter_presence_penalty=0
        azure_openai_client_parameter_stop=None
        azure_openai_client_parameter_stream=False
        generative_model_parameters = {
            'azure_openai_client_parameter_max_tokens': azure_openai_client_parameter_max_tokens,
            'azure_openai_client_parameter_temperature': azure_openai_client_parameter_temperature,
            'azure_openai_client_parameter_top_p': azure_openai_client_parameter_top_p,
            'azure_openai_client_parameter_frequency_penalty': azure_openai_client_parameter_frequency_penalty,
            'azure_openai_client_parameter_presence_penalty': azure_openai_client_parameter_presence_penalty,
            'azure_openai_client_parameter_stop': azure_openai_client_parameter_stop,
            'azure_openai_client_parameter_stream': azure_openai_client_parameter_stream
        }
        return generative_model_parameters

    @staticmethod
    def get_bearer_token_provider(token_provider_endpoint: str):
        # Initialize Azure OpenAI Service client with Entra ID authentication
        bearer_token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            token_provider_endpoint
        )
        return bearer_token_provider

    @staticmethod
    def get_generative_ai_client(endpoint: str, bearer_token_provider, api_version: str):
        generative_ai_client = AzureOpenAI(
            azure_endpoint=endpoint,
            azure_ad_token_provider=bearer_token_provider,
            api_version=api_version,
        )
        return generative_ai_client

    @staticmethod
    def get_async_generative_ai_client(endpoint: str, bearer_token_provider, api_version: str):
        generative_ai_client = AsyncAzureOpenAI(
            azure_endpoint=endpoint,
            azure_ad_token_provider=bearer_token_provider,
            api_version=api_version,
        )
        return generative_ai_client

    @staticmethod
    def get_chat_prompt(prompt: str):
        # IMAGE_PATH = 'YOUR_IMAGE_PATH'
        # encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
        chat_prompt = [
            {
                'role': 'system',
                'content': [
                    {
                        'type': 'text',
                        'text': prompt
                    }
                ]
            }
        ]
        return chat_prompt

    @staticmethod
    def get_generative_ai_completion_using_single_prompt_using_multiple_prompts(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompts):
        # Include speech result if speech is enabled
        generative_ai_completion = generative_ai_client.chat.completions.create(
            model=generative_model_configuration['deployment'],
            messages=prompts,
            max_tokens=generative_model_parameters['azure_openai_client_parameter_max_tokens'],
            temperature=generative_model_parameters['azure_openai_client_parameter_temperature'],
            top_p=generative_model_parameters['azure_openai_client_parameter_top_p'],
            frequency_penalty=generative_model_parameters['azure_openai_client_parameter_frequency_penalty'],
            presence_penalty=generative_model_parameters['azure_openai_client_parameter_presence_penalty'],
            stop=None,
            stream=False
        )
        return generative_ai_completion

    @staticmethod
    def get_generative_ai_completion_using_single_prompt_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt: str):
        # Include speech result if speech is enabled
        messages = OpenaiAzureFoundryUtility.get_chat_prompt(prompt)
        generative_ai_completion = generative_ai_client.chat.completions.create(
            model=generative_model_configuration['deployment'],
            messages=messages,
            max_tokens=generative_model_parameters['azure_openai_client_parameter_max_tokens'],
            temperature=generative_model_parameters['azure_openai_client_parameter_temperature'],
            top_p=generative_model_parameters['azure_openai_client_parameter_top_p'],
            frequency_penalty=generative_model_parameters['azure_openai_client_parameter_frequency_penalty'],
            presence_penalty=generative_model_parameters['azure_openai_client_parameter_presence_penalty'],
            stop=None,
            stream=False
        )
        return generative_ai_completion

    @staticmethod
    def get_chat_response(generative_ai_completion) -> str:
        response_in_json = json.loads(generative_ai_completion.to_json())
        # print('---- DEBUGGING-response_in_json ----', response_in_json)
        response_choices = response_in_json['choices']
        # print('---- DEBUGGING-response_choices ----', response_choices)
        response_choice = response_choices[0]
        # print('---- DEBUGGING-response_choice ----', response_choice)
        response_message = response_choice['message']
        # print('---- DEBUGGING-response_message ----', response_message)
        response_message_content = response_message['content']
        # print('---- DEBUGGING-response_message_content ----', response_message_content)
        response_payload = GenerativeAiResponseProcessingUtility.extract_generated_python_code(
            response_message_content)
        # print('---- DEBUGGING-response_payload ----', response_payload)
        return response_payload

async def main_test_happy_path():
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    prompt = PromptOperationsResearchExampleRepository.FarmerOptimizationProblemWithOrToolsOptimizationProblemAddon
    generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt)
    response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
    print('---- DEBUGGING-response_payload ----', response_payload)
    code_block = response_payload['code_block']
    code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block)
    print('---- DEBUGGING-code_block_execution_result ----', code_block_execution_result)
    code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective(
        code_block_execution_result['message'],
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print('---- DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)

async def main_test_happy_path_AircraftAssignmentProblem():
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    prompt = PromptOperationsResearchExampleRepository.AircraftAssignmentProblemOptimizationProblemWithOrToolsOptimizationProblemAddon
    generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt)
    response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
    print('---- DEBUGGING-response_payload ----', response_payload)
    code_block = response_payload['code_block']
    code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block)
    print('---- DEBUGGING-code_block_execution_result ----', code_block_execution_result)
    code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective(
        code_block_execution_result['message'],
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print('---- DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)

async def main_test_happy_path_FisheryOptimizationProblem():
    to_delete_python_code: bool = True
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    prompt = PromptOperationsResearchExampleRepository.FisheryOptimizationProblemOptimizationProblemWithOrToolsOptimizationProblemAddon
    generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt)
    response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
    print('---- DEBUGGING-response_payload ----', response_payload)
    code_block = response_payload['code_block']
    code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block, to_delete_python_code, 'generated_using_gpt_4o_azure_foundry_FisheryOptimization_with_addon_prompt_a.py')
    print('---- DEBUGGING-code_block_execution_result ----', code_block_execution_result)
    code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective(
        code_block_execution_result['message'],
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print('---- DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)
    # ---- NOTE-FOR-REFERENCE ---- ValueError: Operators "<" and ">" not supported with the linear solver

async def main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem():
    to_delete_python_code: bool = False
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    file_path_to_problem_sets: str = os.path.join('problem_sets', 'lpwp_combined_result.json')
    problem_sets = ProblemSetsUtility.load_problem_sets(file_path_to_problem_sets)
    problem_0_question = problem_sets['0']['question']
    problem_0_answer = problem_sets['0']['answer']
    print('---- DEBUGGING-problem_0_question ----', problem_0_question)
    print('---- DEBUGGING-problem_0_answer ----', problem_0_answer)
    prompt = f'{problem_0_question} {PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddon}'
    print('---- DEBUGGING-prompt ----', prompt)
    generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt)
    response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
    print('---- DEBUGGING-response_payload ----', response_payload)
    code_block = response_payload['code_block']
    code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block, to_delete_python_code)
    print('---- DEBUGGING-code_block_execution_result ----', code_block_execution_result)
    code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective(
        code_block_execution_result['message'],
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print('---- DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)

async def main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem_and_error_avoidance():
    to_delete_python_code: bool = False
    generative_model_configuration = OpenaiAzureFoundryUtility.get_generative_model_configuration()
    generative_model_parameters = OpenaiAzureFoundryUtility.get_generative_model_parameters()
    bearer_token_provider = OpenaiAzureFoundryUtility.get_bearer_token_provider(generative_model_configuration['token_provider_endpoint'])
    generative_ai_client = OpenaiAzureFoundryUtility.get_generative_ai_client(generative_model_configuration['endpoint'], bearer_token_provider, generative_model_configuration['api_version'])
    file_path_to_problem_sets: str = os.path.join('problem_sets', 'lpwp_combined_result.json')
    problem_sets = ProblemSetsUtility.load_problem_sets(file_path_to_problem_sets)
    problem_0_question = problem_sets['0']['question']
    problem_0_answer = problem_sets['0']['answer']
    print('---- DEBUGGING-problem_0_question ----', problem_0_question)
    print('---- DEBUGGING-problem_0_answer ----', problem_0_answer)
    prompt = f'{problem_0_question} {PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddon}'
    print('---- DEBUGGING-prompt ----', prompt)
    generative_ai_completion = OpenaiAzureFoundryUtility.get_generative_ai_completion_using_single_prompt(
        generative_ai_client,
        generative_model_configuration,
        generative_model_parameters,
        prompt)
    response_payload = OpenaiAzureFoundryUtility.get_chat_response(generative_ai_completion)
    print('---- DEBUGGING-response_payload ----', response_payload)
    code_block = response_payload['code_block']
    code_block_execution_result = await PythonCodeRunnerUtility.async_run_python_code(code_block, to_delete_python_code)
    print('---- DEBUGGING-code_block_execution_result ----', code_block_execution_result)
    code_block_execution_result_message = code_block_execution_result['message']
    print('---- DEBUGGING-code_block_execution_result_message ----', code_block_execution_result_message)
    code_block_execution_result_message_value_error_detection = GenerativeAiResponseProcessingUtility.extract_python_ortools_code_execution_errors(
        code_block_execution_result_message)
    print('---- DEBUGGING-code_block_execution_result_message_value_error_detection ----', code_block_execution_result_message_value_error_detection)
    code_block_execution_result_objective = GenerativeAiResponseProcessingUtility.extract_objective(
        code_block_execution_result_message,
        PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumProfit)
    print('---- DEBUGGING-code_block_execution_result_objective ----', code_block_execution_result_objective)

if __name__ == "__main__":
    # asyncio.run(main_test_happy_path())
    # asyncio.run(main_test_happy_path_AircraftAssignmentProblem())
    # asyncio.run(main_test_happy_path_FisheryOptimizationProblem())
    asyncio.run(main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem())
    # asyncio.run(main_test_happy_path_with_problem_sets_0_FisheryOptimizationProblem_and_error_avoidance())
