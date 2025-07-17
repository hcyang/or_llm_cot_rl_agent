from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_sd, F_tr, C_sd, C_tr, Budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    solver.Add(C_sd * x + C_tr * y <= Budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Define the objective function
    solver.Maximize(F_sd * x + F_tr * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Number of sled dog trips (x): {x.solution_value()}')
        print(f'Number of truck trips (y): {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage with hypothetical values
F_sd = 100  # Number of fish per sled dog trip
F_tr = 300  # Number of fish per truck trip
C_sd = 50   # Cost per sled dog trip
C_tr = 150  # Cost per truck trip
Budget = 2000  # Total budget

maximize_fish_transport(F_sd, F_tr, C_sd, C_tr, Budget)
