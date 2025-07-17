from ortools.linear_solver import pywraplp

def solve_transportation_problem(fish_per_sled, fish_per_truck, cost_sled, cost_truck, budget):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None

    # Define the variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    # Total cost constraint
    solver.Add(cost_sled * x + cost_truck * y <= budget)

    # Sled trips must be less than truck trips
    solver.Add(x <= y - 1)

    # Define the objective function
    solver.Maximize(fish_per_sled * x + fish_per_truck * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage
fish_per_sled = 100
fish_per_truck = 200
cost_sled = 500
cost_truck = 1000
budget = 10000

solve_transportation_problem(fish_per_sled, fish_per_truck, cost_sled, cost_truck, budget)
