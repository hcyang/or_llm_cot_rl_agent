from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_d, f_t, c_d, c_t, B):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None

    # Decision variables
    x = solver.IntVar(0.0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0.0, solver.infinity(), 'y')  # Number of truck trips

    # Objective function: maximize f_d * x + f_t * y
    solver.Maximize(f_d * x + f_t * y)

    # Constraints
    # Budget constraint: c_d * x + c_t * y <= B
    solver.Add(c_d * x + c_t * y <= B)

    # Sled dog trips must be less than truck trips: x < y
    solver.Add(x <= y - 1)  # Using <= y - 1 to represent x < y

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value (maximized fish): {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters
f_d = 100  # fish per sled dog trip
f_t = 300  # fish per truck trip
c_d = 50   # cost per sled dog trip
c_t = 100  # cost per truck trip
B = 1000   # total budget

# Run the optimization
maximize_fish_transport(f_d, f_t, c_d, c_t, B)
