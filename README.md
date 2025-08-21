# or_llm_cot_rl_agent

## Introduction
The goal of this project is to read a free-form text description of an Operations Research (OR) problem and generate a Python program that can run and find an (near) optimized solution.

## How to run
The entry-point "main" program is in
- automated_generative_ai_prompt_engineering_feedback_loop_learner\automated_generative_ai_prompt_engineering_feedback_loop_learner.py

You can open the project foder and the program in Visual Studio Code, then pull down Run and click 'Run Without Debugging'.

Below are several parameters for accessing a LLM model hosted in Azure Open AI. You would need to set them up as environment variables:
- ENDPOINT_URL
- DEPLOYMENT_NAME
- TOKEN_PROVIDER_ENDPOINT_URL
- API_VERSION

## Project structure
- generated: folder for storing generated Python OR programs
- problem_sets: input problem descriptions
- utility_debugging: Python utility routines for debugging purposes
- utility_openai: Pytjon utility routines for accessing openai
- utility_ollama: Python utility routines for ollama models
- utility_problem_sets: Python utility routines for accessing problem_sets instances
- utility_prompt_engineering: Python utility routines for prompt engineering
- utility_python: common Python routines.
- utility_response_processor: Python utility routines for processing responses from running a Python program.


