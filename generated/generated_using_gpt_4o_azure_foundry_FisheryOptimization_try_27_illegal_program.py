from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_sled, f_truck, c_sled, c_truck, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(f_sled * x + f_truck * y)

    # Add constraints
    solver.Add(c_sled * x + c_truck * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips

    # Solve the problem
    status = solver.Solve()

    # Check if a solution was found
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Optimal solution found:')
        print(f'Number of sled dog trips (x): {x.solution_value()}')
        print(f'Number of truck trips (y): {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('No optimal solution found.')
        return None

# Example parameters
f_sled = 100    # Example fish per sled dog trip
f_truck = 300   # Example fish per truck trip
c_sled = 50     # Example cost per sled dog trip
c_truck = 100   # Example cost per truck trip
budget = 1000   # Example budget

maximize_fish_transport(f_sled, f_truck, c_sled, c_truck, budget)
