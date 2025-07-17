from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips
    
    # Objective function
    solver.Maximize(a * x + b * y)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x) =', x.solution_value())
        print('Number of truck trips (y) =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 300  # Fish per truck trip
c = 10   # Cost per sled dog trip
d = 50   # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
