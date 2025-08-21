from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not available.")
        return

    # Define variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define constraints
    # Constraint 1: Cost budget upper limit
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)

    # Constraint 2: Number of sled dog trips must be less than the number of truck trips
    # Since "<" is not supported, we rewrite it as "sled_dog_trips + 1 <= truck_trips"
    solver.Add(sled_dog_trips + 1 <= truck_trips)

    # Define the objective function
    # Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check the result and display
    if status == pywraplp.Solver.OPTIMAL:
        print(f"OBJECTIVE={solver.Objective().Value()}")
        print(f"Sled dog trips: {sled_dog_trips.solution_value()}")
        print(f"Truck trips: {truck_trips.solution_value()}")
    else:
        print("The problem does not have an optimal solution.")

# Run the function
maximize_fish_transport()
