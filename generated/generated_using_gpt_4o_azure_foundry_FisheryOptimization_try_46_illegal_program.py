from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_s, f_t, c_s, c_t, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Define the constraints
    solver.Add(c_s * x + c_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Define the objective function
    objective = solver.Maximize(f_s * x + f_t * y)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x):', x.solution_value())
        print('Number of truck trips (y):', y.solution_value())
        print('Maximized number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage
# Define parameters
f_s = 50  # Fish per sled dog trip
f_t = 200  # Fish per truck trip
c_s = 100  # Cost per sled dog trip
c_t = 500  # Cost per truck trip
B = 5000  # Budget

maximize_fish_transport(f_s, f_t, c_s, c_t, B)
