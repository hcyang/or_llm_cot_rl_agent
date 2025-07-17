from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the linear solver with the CBC backend
    solver = pywraplp.Solver.CreateSolver('CBC')

    # Define the decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Define the constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage with hypothetical values
a = 100  # Amount of fish per sled dog trip
b = 200  # Amount of fish per truck trip
c = 50   # Cost per sled dog trip
d = 150  # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
