from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_s, f_t, c_s, c_t, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(f_s * x + f_t * y)

    # Define the constraints
    # Cost constraint
    solver.Add(c_s * x + c_t * y <= B)

    # Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
# Example parameters
f_s = 100  # Fish per sled dog trip
f_t = 200  # Fish per truck trip
c_s = 50   # Cost per sled dog trip
c_t = 100  # Cost per truck trip
B = 1000   # Budget

maximize_fish_transport(f_s, f_t, c_s, c_t, B)
