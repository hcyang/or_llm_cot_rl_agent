
import os

import requests
import json
import re

from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository

from utility_response_processor.utility_generative_ai_response_processor import GenerativeAiResponseProcessingUtility

# REFERENCE: https://github.com/ollama/ollama
# REFERENCE: https://github.com/ollama/ollama/blob/main/docs/api.md

class OllamaUtility:
    @staticmethod
    def get_endpoint_url_generate(url_domain: str = 'localhost', url_port: int = 11434) -> str:
        url_generate: str = f'http://{url_domain}:{str(url_port)}/api/generate'
        return url_generate
    @staticmethod
    def get_endpoint_url_chat(url_domain: str = 'localhost', url_port: int = 11434) -> str:
        url_chat: str = f'http://{url_domain}:{str(url_port)}/api/chat'
        return url_chat

    @staticmethod
    def get_payload_headers() -> dict[str, str]:
        headers: dict[str, str] = {
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def get_payload_prompt(model: str, prompt: str, do_return_stream: bool = False) -> str:
        payload_prompt: dict[str, any] = {
            'model': model,
            'prompt': prompt,
            # ---- NOTE-EXPERIMENTAL ---- 'options': { 'num_ctx': 128000 },
            # ---- NOTE-EXPERIMENTAL ---- 'eos_token_id': [128001, 128008, 128009],
            'stream': do_return_stream
        }
        payload_prompt_in_json = json.dumps(payload_prompt)
        # print('---- payload_prompt_in_json:', payload_prompt_in_json)
        return payload_prompt_in_json

    @staticmethod
    def request_response(endpoint_url: str, payload_prompt: str, payload_headers: dict[str, str], do_response_in_json: bool = True) -> object:
        # print('---- endpoint_url:', endpoint_url)
        # print('---- payload_prompt:', payload_prompt)
        # print('---- payload_headers:', payload_headers)
        response_generate = requests.post(endpoint_url, headers=payload_headers, data=payload_prompt)
        if response_generate.status_code == 200:
            response_payload = json.loads(response_generate.content) if do_response_in_json else response_generate
            # print('SUCCESS:', response_payload)
            # print('SUCCESS:', response_generate.status_code)
            return response_payload
        else:
            response_payload = '' if do_response_in_json else response_generate
            # print('ERROR:', response_generate.status_code)
            # print('ERROR:', response_generate.content)
            return response_payload

    @staticmethod
    def request_response_direct_generate_json(model: str, prompt: str, do_return_stream: bool = False, do_response_in_json: bool = True, url_domain: str = 'localhost', url_port: int = 11434) -> str:
        endpoint_url: str = OllamaUtility.get_endpoint_url_generate(url_domain, url_port)
        payload_headers: dict[str, str] = OllamaUtility.get_payload_headers()
        payload_prompt: str = OllamaUtility.get_payload_prompt(model, prompt, do_return_stream)
        response = OllamaUtility.request_response(
            endpoint_url=endpoint_url,
            payload_prompt=payload_prompt,
            payload_headers=payload_headers,
            do_response_in_json=do_response_in_json)
        return response

# REFERENCE: https://en.wikipedia.org/wiki/Linear_programming
def main_test_lp_problem():
    model = 'llama3.2'
    prompt = PromptOperationsResearchExampleRepository.FarmerOptimizationProblemWithOrToolsOptimizationProblemAddon
    response_payload = OllamaUtility.request_response_direct_generate_json(
        model,
        prompt)
    # print(response_payload['response'])
    response_payload_python_code = response_payload['response']
    extracted_python_code = GenerativeAiResponseProcessingUtility.extract_generated_python_code(response_payload_python_code)
    print(extracted_python_code)

# REFERENCE: https://en.wikipedia.org/wiki/Linear_programming
def main_test_lp_problem_shortened():
    model = 'llama3.2'
    prompt = PromptOperationsResearchExampleRepository.FarmerOptimizationProblemWithOrToolsOptimizationProblemAddon
    response_payload = OllamaUtility.request_response_direct_generate_json(
        model,
        prompt)
    print(response_payload['response'])

def main_test_happy_path():
    model = 'llama3.2'
    prompt = 'What is water made of? Respond using JSON'
    response_payload = OllamaUtility.request_response_direct_generate_json(
        model,
        prompt)
    print(response_payload['response'])

if __name__ == "__main__":
    main_test_lp_problem()
    # main_test_lp_problem_shortened()
    # main_test_happy_path()
