
import os

import requests
import json
import re

from utility_prompt_engineering.prompt_operations_research_example_repository import PromptOperationsResearchExampleRepository
from utility_response_processor.utility_generative_ai_response_processor import GenerativeAiResponseProcessingUtility

class GenerativeAiResponseProcessingForFisherOptimizationProblemUtility:
    @staticmethod
    def extract_objective(code_execution_output_text: str, make_lower_before_matching: bool = True) -> float:
        """
        """
        objective_prefix = PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixMaximumNumberOfFishTransported
        objective = GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix, make_lower_before_matching)
        if objective is not None:
            return objective
        objective_prefix = PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixTotalFishTransported
        objective = GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix, make_lower_before_matching)
        if objective is not None:
            return objective
        objective_prefix = PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixObjectiveValueMaximizedFish
        objective = GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix, make_lower_before_matching)
        if objective is not None:
            return objective
        objective_prefix = PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixObjectiveValueTotalFish
        objective = GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix, make_lower_before_matching)
        if objective is not None:
            return objective
        objective_prefix = PromptOperationsResearchExampleRepository.ObjectiveSearchQueryPrefixObjectiveScoreMaximizedFishTransported
        objective = GenerativeAiResponseProcessingUtility.extract_objective(code_execution_output_text, objective_prefix, make_lower_before_matching)
        if objective is not None:
            return objective
        return None

if __name__ == "__main__":
    pass
