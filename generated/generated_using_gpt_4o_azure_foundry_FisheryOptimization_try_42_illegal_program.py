from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c_s, c_t, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Define variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Objective function: Maximize a*x + b*y
    solver.Maximize(a * x + b * y)

    # Constraints
    # 1. Cost constraint
    solver.Add(c_s * x + c_t * y <= B)

    # 2. Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example values
a = 50  # Fish per sled dog trip
b = 200  # Fish per truck trip
c_s = 10  # Cost per sled dog trip
c_t = 50  # Cost per truck trip
B = 1000  # Total budget

maximize_fish_transport(a, b, c_s, c_t, B)
