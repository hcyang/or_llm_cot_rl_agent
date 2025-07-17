from ortools.linear_solver import pywraplp

def solve_fishery_transportation():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('CBC')

    # Define the variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define the constraints
    # Constraint: Cost budget should not exceed 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # Constraint: Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Define the objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check if a solution exists
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE={solver.Objective().Value()}')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
    else:
        print('No optimal solution found.')

# Execute the function to solve the problem
solve_fishery_transportation()
