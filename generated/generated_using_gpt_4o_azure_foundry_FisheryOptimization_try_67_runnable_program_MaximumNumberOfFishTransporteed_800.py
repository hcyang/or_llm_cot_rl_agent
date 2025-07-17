from ortools.linear_solver import pywraplp

def maximize_fish_transportation(budget, sled_dog_cost, truck_cost, sled_dog_capacity, truck_capacity):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print('Solver not created.')
        return

    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Constraints
    # 1. Budget constraint
    solver.Add(sled_dog_cost * x + truck_cost * y <= budget)

    # 2. Sled dog trips must be less than truck trips
    solver.Add(x <= y - 1)

    # Objective function: maximize the total number of fish transported
    solver.Maximize(sled_dog_capacity * x + truck_capacity * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage
budget = 1000  # Total budget available
sled_dog_cost = 50  # Cost per sled dog trip
truck_cost = 100  # Cost per truck trip
sled_dog_capacity = 30  # Fish transported per sled dog trip
truck_capacity = 80  # Fish transported per truck trip

maximize_fish_transportation(budget, sled_dog_cost, truck_cost, sled_dog_capacity, truck_capacity)
