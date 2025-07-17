from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget):
    # Create a solver using the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Decision variables: number of trips by sled dogs and trucks
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips

    # Objective: Maximize the total number of fish transported
    solver.Maximize(fish_per_sled * x + fish_per_truck * y)

    # Constraints:
    # 1. Total cost should not exceed the budget
    solver.Add(cost_per_sled * x + cost_per_truck * y <= budget)

    # 2. Number of sled dog trips must be less than the number of truck trips
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example input
fish_per_sled = 100
fish_per_truck = 300
cost_per_sled = 500
cost_per_truck = 1500
budget = 10000

maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget)
