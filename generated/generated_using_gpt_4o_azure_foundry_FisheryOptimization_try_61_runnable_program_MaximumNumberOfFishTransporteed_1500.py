from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    # Cost constraint
    solver.Add(c * x + d * y <= B)
    
    # Sled dog trips must be less than truck trips
    solver.Add(x <= y - 1)  # x < y is equivalent to x <= y - 1
    
    # Define the objective function
    solver.Maximize(a * x + b * y)

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

# Example parameters
a = 50  # Fish per sled dog trip
b = 100  # Fish per truck trip
c = 10  # Cost per sled dog trip
d = 20  # Cost per truck trip
B = 300  # Budget

maximize_fish_transport(a, b, c, d, B)
