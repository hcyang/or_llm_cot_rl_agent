from ortools.linear_solver import pywraplp

def solve_fishery_transportation(a, b, c_d, c_t, B):
    # Create the linear solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(a * x + b * y)
    
    # Constraints
    # Cost constraint
    solver.Add(c_d * x + c_t * y <= B)
    
    # Number of trips constraint
    solver.Add(x < y)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Number of sled dog trips (x): {x.solution_value()}')
        print(f'Number of truck trips (y): {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage with hypothetical values
solve_fishery_transportation(a=100, b=200, c_d=50, c_t=150, B=1000)
