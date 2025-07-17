from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_s, F_t, C_s, C_t, B):
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables s and t.
    s = solver.NumVar(0, solver.infinity(), 's')
    t = solver.NumVar(0, solver.infinity(), 't')

    # Define the objective: maximize F_s * s + F_t * t
    solver.Maximize(F_s * s + F_t * t)

    # Add the budget constraint.
    solver.Add(C_s * s + C_t * t <= B)

    # Add the sled dog trips constraint.
    solver.Add(s < t)

    # Solve the problem.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'Number of sled dog trips: {s.solution_value()}')
        print(f'Number of truck trips: {t.solution_value()}')
        print(f'OBJECTIVE= {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example values for the parameters
F_s = 100  # Amount of fish per sled dog trip
F_t = 300  # Amount of fish per truck trip
C_s = 10   # Cost per sled dog trip
C_t = 50   # Cost per truck trip
B = 1000   # Budget limit

maximize_fish_transport(F_s, F_t, C_s, C_t, B)
