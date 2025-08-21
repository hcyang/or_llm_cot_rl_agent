import json
import os
import sys
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from utility_debugging.utility_debugging import DebuggingUtility
from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository
from utility_response_processor.utility_generative_ai_response_processor import GenerativeAiResponseProcessingUtility

endpoint = os.getenv('ENDPOINT_URL', '')
if endpoint == '':
    DebuggingUtility.error('The environment variable ENDPOINT_URL has not been set yet.')
    sys.exit(1)
deployment = os.getenv('DEPLOYMENT_NAME', '')
if deployment == '':
    DebuggingUtility.error('The environment variable DEPLOYMENT_NAME has not been set yet.')
    sys.exit(1)
token_provider_endpoint = os.getenv('TOKEN_PROVIDER_ENDPOINT_URL', '')
if token_provider_endpoint == '':
    DebuggingUtility.error('The environment variable TOKEN_PROVIDER_ENDPOINT_URL has not been set yet.')
    sys.exit(1)
api_version = os.getenv('API_VERSION', '')
if api_version == '':
    DebuggingUtility.error("The environment variable API_VERSION has not been set yet.")
    sys.exit(1)

azure_openai_client_parameter_max_tokens=800
azure_openai_client_parameter_temperature=0.7
azure_openai_client_parameter_top_p=0.95
azure_openai_client_parameter_frequency_penalty=0
azure_openai_client_parameter_presence_penalty=0
azure_openai_client_parameter_stop=None
azure_openai_client_parameter_stream=False

# Initialize Azure OpenAI Service client with Entra ID authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    token_provider_endpoint
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version=api_version,
)

# IMAGE_PATH = 'YOUR_IMAGE_PATH'
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
chat_prompt = [
    {
        'role': 'system',
        'content': [
            {
                'type': 'text',
                'text': PromptOperationsResearchExampleRepository.FarmerOptimizationProblemWithOrToolsOptimizationProblemAddon
            }
        ]
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=azure_openai_client_parameter_max_tokens,
    temperature=azure_openai_client_parameter_temperature,
    top_p=azure_openai_client_parameter_top_p,
    frequency_penalty=azure_openai_client_parameter_frequency_penalty,
    presence_penalty=azure_openai_client_parameter_presence_penalty,
    stop=None,
    stream=False
)

response_in_json = json.loads(completion.to_json())
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
print('---- DEBUGGING-response_payload ----', response_payload)
