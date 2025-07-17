from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_d, F_t, C_d, C_t, B):
    # Create the solver using the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Define the variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    solver.Add(C_d * x + C_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Define the objective
    solver.Maximize(F_d * x + F_t * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters
F_d = 10  # Fish per sled dog trip
F_t = 50  # Fish per truck trip
C_d = 100  # Cost per sled dog trip
C_t = 500  # Cost per truck trip
B = 5000   # Total budget

maximize_fish_transport(F_d, F_t, C_d, C_t, B)
