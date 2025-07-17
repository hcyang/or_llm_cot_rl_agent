from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver instance
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Constants
    fish_per_sled_dog_trip = 30  # Amount of fish per sled dog trip
    fish_per_truck_trip = 100    # Amount of fish per truck trip
    cost_per_sled_dog_trip = 200  # Cost per sled dog trip
    cost_per_truck_trip = 500     # Cost per truck trip
    budget_limit = 5000           # Total budget

    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Objective: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, fish_per_sled_dog_trip)
    objective.SetCoefficient(truck_trips, fish_per_truck_trip)
    objective.SetMaximization()

    # Constraints
    # Budget constraint
    solver.Add(sled_dog_trips * cost_per_sled_dog_trip +
               truck_trips * cost_per_truck_trip <= budget_limit)

    # Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips <= truck_trips)

    # Solve the problem
    solver.Solve()

    # Print the solution
    print("Number of sled dog trips:", sled_dog_trips.solution_value())
    print("Number of truck trips:", truck_trips.solution_value())
    print("OBJECTIVE=", objective.Value())

# Run the function
maximize_fish_transport()
