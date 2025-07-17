
import asyncio
import os
import json
import re
import subprocess
import sys
import tempfile

class PromptOperationsResearchPhrases:
    OrToolsOptimizationProblemAddon = 'Please write a Python program using OR-Tools that will return a solution with an objective score, which should always be displayed as OBJECTIVE='
    OrToolsOptimizationProblemAddonWithMixedIntegerProgramSpecific = 'Please write a Python program using OR-Tools mixed-integer programming solver that will return a solution with an objective score, which should always be displayed as OBJECTIVE='
    PleaseImporveTheGeneratedCodeWithBetterSolutionWithHigherObjectiveScore = 'Please improve the generated code that can produce a better solution with a higher objective score'
    PleaseExamineTheGeneratedCodeAndFixAnyBuildErrors = 'The generated program has errors, Please examine the generated code and fix any errors'
