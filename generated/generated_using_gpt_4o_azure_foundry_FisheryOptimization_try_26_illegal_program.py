from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips
    
    # Coefficients
    a = 10  # fish per sled dog trip
    b = 40  # fish per truck trip
    c = 100  # cost per sled dog trip
    d = 500  # cost per truck trip
    budget = 5000  # total budget
    
    # Objective function: Maximize a * x + b * y
    solver.Maximize(a * x + b * y)
    
    # Constraints
    # Cost constraint
    solver.Add(c * x + d * y <= budget)
    
    # Number of trips constraint
    solver.Add(x < y)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x):', x.solution_value())
        print('Number of truck trips (y):', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

maximize_fish_transport()
