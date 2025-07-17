from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    # Number of sled dog trips
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    # Number of truck trips
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Define the parameters
    fish_per_sled_dog_trip = 10
    fish_per_truck_trip = 50
    cost_per_sled_dog_trip = 100
    cost_per_truck_trip = 200
    budget_limit = 1000

    # Objective function: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, fish_per_sled_dog_trip)
    objective.SetCoefficient(truck_trips, fish_per_truck_trip)
    objective.SetMaximization()

    # Budget constraint
    solver.Add(cost_per_sled_dog_trip * sled_dog_trips +
               cost_per_truck_trip * truck_trips <= budget_limit)

    # Constraint: Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Solve the problem
    solver.Solve()

    # Output the solution
    print(f'SLED DOG TRIPS: {sled_dog_trips.solution_value()}')
    print(f'TRUCK TRIPS: {truck_trips.solution_value()}')
    print(f'OBJECTIVE= {objective.Value()}')

maximize_fish_transport()
