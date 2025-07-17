from ortools.linear_solver import pywraplp

def solve_fish_transport(a, b, c1, c2, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Objective function
    solver.Maximize(a * x + b * y)
    
    # Constraints
    solver.Add(c1 * x + c2 * y <= budget)
    solver.Add(x < y)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum number of fish transported =', a * x.solution_value() + b * y.solution_value())
        return a * x.solution_value() + b * y.solution_value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
a = 100  # Number of fish per sled dog trip
b = 200  # Number of fish per truck trip
c1 = 50  # Cost per sled dog trip
c2 = 100  # Cost per truck trip
budget = 1000  # Total budget

solve_fish_transport(a, b, c1, c2, budget)
