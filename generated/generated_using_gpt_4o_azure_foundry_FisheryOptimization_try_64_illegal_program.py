from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget_limit):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Constraints
    solver.Add(x < y)  # Sled dog trips must be less than truck trips
    solver.Add(cost_per_sled * x + cost_per_truck * y <= budget_limit)  # Budget constraint

    # Objective
    objective = solver.Maximize(fish_per_sled * x + fish_per_truck * y)

    # Solve the problem
    status = solver.Solve()

    # Check if the solution is optimal
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
maximize_fish_transport(
    fish_per_sled=100,  # Example value for fish per sled trip
    fish_per_truck=200,  # Example value for fish per truck trip
    cost_per_sled=50,  # Example value for cost per sled trip
    cost_per_truck=100,  # Example value for cost per truck trip
    budget_limit=1000  # Example budget limit
)
