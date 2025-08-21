
import os
import sys
from openai import AzureOpenAI  

from utility_debugging.utility_debugging import DebuggingUtility
from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository

endpoint = os.getenv('ENDPOINT_URL', '')  
if endpoint == "":
    DebuggingUtility.error('The environment variable ENDPOINT_URL has not been set yet.')
    sys.exit(1)
deployment = os.getenv('DEPLOYMENT_NAME', '')  
if deployment == "":
    DebuggingUtility.error('The environment variable DEPLOYMENT_NAME has not been set yet.')
    sys.exit(1)
subscription_key = os.getenv('AZURE_OPENAI_API_KEY', '')  
if subscription_key == "":
    DebuggingUtility.error('The environment variable AZURE_OPENAI_API_KEY has not been set yet.')
    sys.exit(1)
api_version = os.getenv('API_VERSION', '')
if api_version == "":
    DebuggingUtility.error("The environment variable API_VERSION has not been set yet.")
    sys.exit(1)

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version=api_version,
)
    
    
# IMAGE_PATH = 'YOUR_IMAGE_PATH'
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Prepare the chat prompt 
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
    
# Generate the completion  
completion = client.chat.completions.create(  
    model=deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False
)

print(completion.to_json())  
    