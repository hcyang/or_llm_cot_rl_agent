from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_s, f_t, c_s, c_t, budget):
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None

    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Objective function: maximize f_s * x + f_t * y
    solver.Maximize(f_s * x + f_t * y)

    # Constraint 1: c_s * x + c_t * y <= budget
    solver.Add(c_s * x + c_t * y <= budget)

    # Constraint 2: x < y
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    # Check the solution status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x) =', x.solution_value())
        print('Number of truck trips (y) =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example data
f_s = 50  # Fish per sled dog trip
f_t = 200  # Fish per truck trip
c_s = 100  # Cost per sled dog trip
c_t = 300  # Cost per truck trip
budget = 5000  # Total budget

maximize_fish_transport(f_s, f_t, c_s, c_t, budget)
