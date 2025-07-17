from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None
    
    # Define variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips
    
    # Objective function: maximize ax + by
    solver.Maximize(a * x + b * y)
    
    # Constraints
    # 1. Cost constraint: cx + dy <= B
    solver.Add(c * x + d * y <= B)
    
    # 2. Sled dog trips constraint: x < y
    solver.Add(x < y)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value (Max fish transported) =', solver.Objective().Value())
        print('Sled dog trips =', x.solution_value())
        print('Truck trips =', y.solution_value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage with made-up data:
a = 100  # Fish per sled dog trip
b = 300  # Fish per truck trip
c = 20   # Cost per sled dog trip
d = 50   # Cost per truck trip
B = 1000 # Total budget

maximize_fish_transport(a, b, c, d, B)
