from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Add constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Solve the problem
    result_status = solver.Solve()

    # Check the result status
    if result_status == pywraplp.Solver.OPTIMAL:
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example values for a, b, c, d, budget
a = 100  # fish per sled dog trip
b = 200  # fish per truck trip
c = 50   # cost per sled dog trip
d = 100  # cost per truck trip
budget = 1000  # total budget

maximize_fish_transport(a, b, c, d, budget)
