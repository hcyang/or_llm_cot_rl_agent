
import asyncio
import os
import json
import re
import subprocess
import sys
import tempfile

# REFERENCE: https://docs.python.org/3/library/typing.html
import typing

type Prompt = dict[str, str|list[str, str]]
type Prompts = list[Prompt]

# REFERENCE: https://arize.com/blog-course/mastering-openai-api-tips-and-tricks/
#     Explanation of Roles in Messages
#     Within the OpenAI API, messages often adopt specific roles to guide the model’s responses.
#     Commonly used roles include “system,” “user,” and “assistant.”
#     The “system” provides high-level instructions,
#     the “user” presents queries or prompts,
#     and the “assistant” is the model’s response.
#     By differentiating these roles, we can set the context and direct the conversation efficiently.
#     
#     How to Use Roles in Messages to Improve Model Performance
#     Strategic use of roles can significantly enhance the model’s output.
#     
#     Here are some ways to do this:
#     
#     Set Clear Context with System Role: Begin with a system message to define the context or
#     behavior you desire from the model. This acts as a guidepost for subsequent interactions.
#     Explicit User Prompts: Being clear and concise in the user role
#     ensures the model grasps the exact requirement, leading to more accurate responses.
#     Feedback Loop: If the model’s response isn’t satisfactory, use the user role to provide
#     feedback or refine the query, nudging the model towards the desired output.
#     Iterative Conversation: Think of the interaction as a back-and-forth dialogue.
#     By maintaining a sequence of user and assistant messages, the model can reference prior messages, ensuring context is retained.
#     Ultimately, understanding and effectively utilizing roles in messages is
#     akin to having a clear conversation with another human. By setting context and guiding the discourse, we can significantly bolster the performance and relevance of the model’s outputs.
#
# NOTE: Be aware that some models do not generally pay as much attention to the system message equally.
#     For example, gpt-3.5-turbo-0301 does not generally pay as much attention to the system message
#     as gpt-4-0314 or gpt-3.5-turbo-0613

# REFERENCE: https://arize.com/blog-course/mastering-openai-api-tips-and-tricks/
#     Temperature
#     In the realm of OpenAI’s API framework, it is noteworthy to highlight the inherent
#     non-deterministic nature of the model. This characteristic implies that, given a static prompt,
#     the model may yield marginally different completions upon successive invocations.
#     To mitigate this variability, users have the option to adjust the ‘temperature‘ parameter.
#     Setting this parameter to 0 converges the output towards determinism, although minuscule
#     variations can still be observed.
#     
#     Guidance on Temperature Parameter Adjustment
#     The ‘temperature‘ parameter plays a pivotal role in modulating the output’s balance between
#     consistency and novelty. A decrease in its value leans the results towards uniformity and predictability.
#     In contrast, an increment promotes a broader diversity in responses, introducing an element
#     of novelty and creativity. As a best practice, users should calibrate the temperature value
#     commensurate with the desired equilibrium between coherence and innovation specific to their
#     application’s requisites.

# REFERENCE: https://arize.com/blog-course/mastering-openai-api-tips-and-tricks/
#     Function Calling
#     The OpenAI API has evolved over time, introducing a plethora of features to enhance user experience and provide more structured outputs. One such feature that stands out is the “function calling” capability in the Chat Completions API. This feature is not just a mere addition but a game-changer in how developers interact with the model and retrieve structured data.
#     
#     Explanation of Function Calls in OpenAI API
#     Function calling in the OpenAI API is a mechanism that allows models to detect when a specific function needs to be invoked based on the user’s input. Once detected, the model responds with JSON that adheres to the function’s signature. This capability ensures that developers can reliably obtain structured data from the model, enhancing the versatility of applications they can build.
#     
#     For instance, with function calling, developers can:
#     
#     Create chatbots that answer questions by invoking external tools, akin to ChatGPT Plugins.
#     Convert natural language inputs into specific API calls or even database queries.
#     Extract structured data from text, making it easier to process and analyze.
#     How to Use Function Calls to Customize Model Behavior
#     To harness the power of function calling, follow these steps:
#     
#     Define the Function: When calling the model, specify the functions you want to use along with the user’s input. For example, if you want to know the current weather in a specific location, you can use a function like get_current_weather.
#     Model Interaction: The model, upon receiving the function and user’s input, will process the information. If the function is recognized and the input matches its requirements, the model will return a structured response adhering to the function’s signature.
#     Third-Party Integration: In some cases, like the weather example, you might need to integrate with a third-party API. Use the model’s response to call this API and fetch the required data.
#     Send Data Back to Model: Once you have the data from the third-party API, you can send it back to the model for further processing or summarization.
#     For a practical illustration, consider the scenario where a user asks, “What’s the weather like in Boston right now?” Using function calling, the process would look like:
#     
#     Call the model with the get_current_weather function and user’s input.
#     
#     The model responds with a function call to get_current_weather for “Boston, MA”.
#     
#     Use this response to call a third-party weather API.
#     
#     Send the weather data back to the model.
#     
#     The model then summarizes the data, e.g., “The weather in Boston is currently sunny with a temperature of 22 degrees Celsius.”
#     
#     Function calling, in essence, bridges the gap between natural language processing and structured data retrieval, making the OpenAI API a more powerful tool for developers.

class PromptGenerator:
    @staticmethod
    def add_user_prompt(prompts: Prompts, prompt: str):
        prompts.append(PromptGenerator.generate_user_prompt(prompt))
        return prompts

    @staticmethod
    def add_assistant_prompt(prompts: Prompts, prompt: str):
        prompts.append(PromptGenerator.generate_assistant_prompt(prompt))
        return prompts

    @staticmethod
    def add_system_prompt(prompts: Prompts, prompt: str):
        prompts.append(PromptGenerator.generate_system_prompt(prompt))
        return prompts

    @staticmethod
    def generate_user_prompt(prompt: str) -> Prompt:
        return PromptGenerator.generate_prompt('user', prompt)

    @staticmethod
    def generate_assistant_prompt(prompt: str) -> Prompt:
        return PromptGenerator.generate_prompt('assistant', prompt)

    @staticmethod
    def generate_system_prompt(prompt: str) -> Prompt:
        return PromptGenerator.generate_prompt('system', prompt)

    @staticmethod
    def generate_prompt(role: str, prompt: str) -> Prompt:
        return {
            'role': role,
            'content': [
                {
                    'type': 'text',
                    'text': prompt
                }
            ]
        }
