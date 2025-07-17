from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the linear solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        raise Exception("Could not create solver.")
    
    # Variables
    # x: number of sled dog trips (integer)
    # y: number of truck trips (integer)
    x = solver.IntVar(0.0, solver.infinity(), 'x')
    y = solver.IntVar(0.0, solver.infinity(), 'y')
    
    # Constraints
    # Budget constraint
    solver.Add(c * x + d * y <= budget)
    
    # Sled dog trips must be less than truck trips
    solver.Add(x < y)
    
    # Objective function
    solver.Maximize(a * x + b * y)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value (max fish transported): {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')
        
    return solver.Objective().Value()

# Example usage with hypothetical values
a = 100  # fish per sled dog trip
b = 200  # fish per truck trip
c = 50   # cost per sled dog trip
d = 100  # cost per truck trip
budget = 1000  # total budget

maximize_fish_transport(a, b, c, d, budget)
