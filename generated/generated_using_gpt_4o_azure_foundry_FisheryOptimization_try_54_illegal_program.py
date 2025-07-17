from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c1, c2, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Decision variables
    x = solver.IntVar(0.0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0.0, solver.infinity(), 'y')  # Truck trips
    
    # Objective function
    solver.Maximize(a * x + b * y)
    
    # Constraints
    solver.Add(c1 * x + c2 * y <= budget)  # Cost constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example data
a = 100  # Fish per sled dog trip
b = 250  # Fish per truck trip
c1 = 50  # Cost per sled dog trip
c2 = 100  # Cost per truck trip
budget = 1000  # Total budget

# Run the function with given parameters
maximize_fish_transport(a, b, c1, c2, budget)
