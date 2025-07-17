from ortools.linear_solver import pywraplp

def transport_fish(f_s, f_t, c_s, c_t, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    objective = solver.Maximize(f_s * x + f_t * y)

    # Define the constraints
    solver.Add(c_s * x + c_t * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage
f_s = 100  # Example value: sled dogs can carry 100 fish per trip
f_t = 200  # Example value: trucks can carry 200 fish per trip
c_s = 50   # Example value: cost per sled dog trip
c_t = 75   # Example value: cost per truck trip
budget = 1000  # Example value: maximum budget

transport_fish(f_s, f_t, c_s, c_t, budget)
