from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Define decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Define the constraints
    solver.Add(c * x + d * y <= B)  # Budget constraint
    solver.Add(x < y)               # Sled dog trips less than truck trips
    
    # Define the objective function
    solver.Maximize(a * x + b * y)  # Maximize fish transported
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the solution status
    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example parameters
a = 100  # Units of fish per sled dog trip
b = 200  # Units of fish per truck trip
c = 50   # Cost per sled dog trip
d = 150  # Cost per truck trip
B = 1000 # Total budget

maximize_fish_transport(a, b, c, d, B)
