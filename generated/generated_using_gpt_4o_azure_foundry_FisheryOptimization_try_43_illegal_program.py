from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    solver.Add(x * c + y * d <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Solve the problem
    status = solver.Solve()

    # Check the solution status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x):', x.solution_value())
        print('Number of truck trips (y):', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage:
a = 100  # Number of fish per sled dog trip
b = 200  # Number of fish per truck trip
c = 50   # Cost per sled dog trip
d = 150  # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
