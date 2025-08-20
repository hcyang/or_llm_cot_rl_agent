from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        raise Exception("Solver not created. Please ensure OR-Tools is installed correctly.")

    # Define variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define constants
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    cost_budget = 100

    # Define the objective function: maximize the number of fish transported
    solver.Maximize(
        fish_per_sled_dog_trip * sled_dog_trips + fish_per_truck_trip * truck_trips
    )

    # Define constraints
    # Constraint: Total cost must not exceed the budget
    solver.Add(
        cost_per_sled_dog_trip * sled_dog_trips + cost_per_truck_trip * truck_trips <= cost_budget
    )
    # Constraint: Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f"OBJECTIVE={solver.Objective().Value()}")
        print(f"Number of sled dog trips: {sled_dog_trips.solution_value()}")
        print(f"Number of truck trips: {truck_trips.solution_value()}")
    else:
        print("The solver did not find an optimal solution.")

# Run the program
maximize_fish_transport()
