from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Define constraints
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)
    solver.Add(sled_dog_trips < truck_trips)  # Number of sled dog trips must be less than truck trips

    # Define objective function
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, sled_dog_capacity)
    objective.SetCoefficient(truck_trips, truck_capacity)
    objective.SetMaximization()

    # Solve the problem
    solver.Solve()

    # Return the results
    sled_dog_trips_value = sled_dog_trips.solution_value()
    truck_trips_value = truck_trips.solution_value()
    max_fish = objective.Value()

    return sled_dog_trips_value, truck_trips_value, max_fish

# Example parameters
sled_dog_capacity = 100  # Amount of fish per sled dog trip
truck_capacity = 500     # Amount of fish per truck trip
sled_dog_cost = 50       # Cost per sled dog trip
truck_cost = 200         # Cost per truck trip
budget = 1000            # Maximum budget

sled_dog_trips, truck_trips, max_fish = maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget)

print(f"Sled dog trips: {sled_dog_trips}")
print(f"Truck trips: {truck_trips}")
print(f"Maximum fish transported: {max_fish}")
