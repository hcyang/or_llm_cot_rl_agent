from ortools.linear_solver import pywraplp

def solve_fish_transportation(a, b, c, d, B):
    # Create the linear solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(a * x + b * y)
    
    # Constraints
    solver.Add(c * x + d * y <= B)  # Budget constraint
    solver.Add(x < y)               # Sled dog trips must be less than truck trips
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips (x): {x.solution_value()}')
        print(f'Number of truck trips (y): {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example parameters
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 150  # Cost per truck trip
B = 1000 # Budget limit

solve_fish_transportation(a, b, c, d, B)
