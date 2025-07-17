from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_d, F_t, C_d, C_t, B):
    # Create the linear solver using the GLOP backend (for linear programming).
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        return None

    # Define the decision variables.
    x_d = solver.NumVar(0, solver.infinity(), 'x_d')  # Number of sled dog trips
    x_t = solver.NumVar(0, solver.infinity(), 'x_t')  # Number of truck trips

    # Define the objective function: Maximize F_d * x_d + F_t * x_t
    solver.Maximize(F_d * x_d + F_t * x_t)

    # Define the constraints.
    # 1. Budget constraint: C_d * x_d + C_t * x_t <= B
    solver.Add(C_d * x_d + C_t * x_t <= B)

    # 2. Sled dog trips must be less than truck trips: x_d < x_t
    solver.Add(x_d <= x_t - 1)

    # Solve the problem.
    status = solver.Solve()

    # Check the result status.
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Number of sled dog trips: {x_d.solution_value()}')
        print(f'Number of truck trips: {x_t.solution_value()}')
        print(f'Maximized number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage:
F_d = 100  # Number of fish per sled dog trip
F_t = 300  # Number of fish per truck trip
C_d = 20   # Cost per sled dog trip
C_t = 50   # Cost per truck trip
B = 1000   # Total budget available

maximize_fish_transport(F_d, F_t, C_d, C_t, B)
