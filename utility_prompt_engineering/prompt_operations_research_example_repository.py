
import asyncio
import os
import json
import re
import subprocess
import sys
import tempfile

from utility_prompt_engineering.prompt_operations_research_phrases import PromptOperationsResearchPhrases

class PromptOperationsResearchExampleRepository:
    # ------------------------------------------------------------------------
    ObjectiveSearchQueryPrefixMaximumProfit: str = 'Maximum Profit:'
    ObjectiveSearchQueryPrefixObjectiveValueTotalCost: str = 'Objective Value (Total Cost):'
    # ------------------------------------------------------------------------
    FarmerOptimizationProblem: str = 'Suppose that a farmer has a piece of farm land, say L hectares, to be planted with either wheat or barley or some combination of the two. The farmer has F kilograms of fertilizer and P kilograms of pesticide. Every hectare of wheat requires F1 kilograms of fertilizer and P1 kilograms of pesticide, while every hectare of barley requires F2 kilograms of fertilizer and P2 kilograms of pesticide. Let S1 be the selling price of wheat and S2 be the selling price of barley, per hectare. If we denote the area of land planted with wheat and barley by x1 and x2 respectively, then profit can be maximized by choosing optimal values for x1 and x2.'
    FarmerOptimizationProblemWithOrToolsOptimizationProblemAddon: str = f'{FarmerOptimizationProblem} {PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddon}'
    # ------------------------------------------------------------------------
    AircraftAssignmentProblemOptimizationProblem: str = 'The Aircraft Assignment Problem aims to assign aircraft to routes in order to minimize the total cost while satisfying demand constraints with available aircraft. The problem involves a set of aircraft and a set of routes. Given the costs of assigning an aircraft to a route. The objective is to minimize the total cost of the assignment. There are limited available aircraft. It is constrained that the number of each aircraft allocated does not exceed its available number. Given the demand of each route and the capabilities (the largest number of people can be carried) of an aircraft for a route. The demand constraint ensures that the total allocation for each route satisfies the demand. The problem seeks to find the most cost-effective assignment of aircraft to routes.'
    AircraftAssignmentProblemOptimizationProblemWithOrToolsOptimizationProblemAddon: str = f'{AircraftAssignmentProblemOptimizationProblem} {PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddon}'
    # ------------------------------------------------------------------------
    FisheryOptimizationProblemOptimizationProblem: str = 'A fishery wants to transport their catch. They can either use local sled dogs or trucks. Local sled dogs and trucks can take different amount of fish per trip. Also, the cost per trip for sled dogs and truck is also differs. You should note that the budget has an upper limit and the number of sled dog trips must be less than the number of truck trips. Formulate an LP to maximize the number of fish that can be transported.'
    FisheryOptimizationProblemOptimizationProblemWithOrToolsOptimizationProblemAddon: str = f'{FisheryOptimizationProblemOptimizationProblem} {PromptOperationsResearchPhrases.OrToolsOptimizationProblemAddon}'
    # ----
    FisheryOptimizationProblemOptimizationProblemSpecifics: str = 'Sled dogs per trip can transport 100 fish. Truck per trip can transport 200 fish. Cost per trip for sled dogs is 10. Cost per trip for trucks is 30. Cost budget upper limit is 100'
    # ----
    ObjectiveSearchQueryPrefixMaximumNumberOfFishTransported: str = 'Maximum number of fish transported:'
    ObjectiveSearchQueryPrefixObjectiveValueTotalFish: str = 'Objective Value (Total Fish):'
    ObjectiveSearchQueryPrefixObjectiveValueMaximizedFish: str = 'Objective value (maximized fish)'
    ObjectiveSearchQueryPrefixTotalFishTransported: str = 'Total fish transported:'
    ObjectiveSearchQueryPrefixObjectiveScoreMaximizedFishTransported: str = 'Objective score (maximized fish transported) ='
    # ------------------------------------------------------------------------
