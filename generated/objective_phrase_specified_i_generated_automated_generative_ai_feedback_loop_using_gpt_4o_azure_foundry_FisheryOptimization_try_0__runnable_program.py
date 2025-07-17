from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Parameters
    fish_per_sled_trip = 500  # Amount of fish transported per sled dog trip
    fish_per_truck_trip = 1000  # Amount of fish transported per truck trip
    cost_per_sled_trip = 100  # Cost per sled dog trip
    cost_per_truck_trip = 300  # Cost per truck trip
    budget_limit = 10000  # Total budget limit

    # Define the constraints
    # Budget constraint
    solver.Add(cost_per_sled_trip * sled_dog_trips + cost_per_truck_trip * truck_trips <= budget_limit)

    # The number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Define the objective function: Maximize the number of fish transported
    objective = solver.Maximize(fish_per_sled_trip * sled_dog_trips + fish_per_truck_trip * truck_trips)

    # Solve the problem
    solver.Solve()

    # Retrieve the results
    sled_dog_trips_solution = sled_dog_trips.solution_value()
    truck_trips_solution = truck_trips.solution_value()
    objective_value = solver.Objective().Value()

    # Display the results
    print(f"Number of sled dog trips: {sled_dog_trips_solution}")
    print(f"Number of truck trips: {truck_trips_solution}")
    print(f"OBJECTIVE= {objective_value}")

# Run the function
maximize_fish_transport()
