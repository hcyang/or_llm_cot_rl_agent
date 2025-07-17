from ortools.linear_solver import pywraplp

def solve_fish_transportation_problem(F_s, F_t, C_s, C_t, B):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        print("Solver not found.")
        return

    # Variables
    x = solver.IntVar(0.0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0.0, solver.infinity(), 'y')  # Number of truck trips

    # Constraints
    solver.Add(C_s * x + C_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips

    # Objective
    solver.Maximize(F_s * x + F_t * y)

    # Solve
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters for testing:
F_s = 50  # Amount of fish sled dogs can carry per trip
F_t = 200  # Amount of fish trucks can carry per trip
C_s = 100  # Cost per trip for sled dogs
C_t = 300  # Cost per trip for trucks
B = 5000  # Total budget

# Solve the problem
solve_fish_transportation_problem(F_s, F_t, C_s, C_t, B)
