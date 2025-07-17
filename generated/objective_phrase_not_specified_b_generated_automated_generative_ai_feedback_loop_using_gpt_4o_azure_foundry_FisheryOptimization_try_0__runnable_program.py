from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Instantiate a Glop linear solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Parameters
    fish_per_sled_dog_trip = 50    # Amount of fish sled dogs can transport per trip
    fish_per_truck_trip = 200      # Amount of fish trucks can transport per trip
    cost_per_sled_dog_trip = 100   # Cost per sled dog trip
    cost_per_truck_trip = 300      # Cost per truck trip
    budget = 5000                  # Total budget available

    # Objective: Maximize the total fish transported
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, fish_per_sled_dog_trip)
    objective.SetCoefficient(truck_trips, fish_per_truck_trip)
    objective.SetMaximization()

    # Constraints
    # Budget constraint
    solver.Add(sled_dog_trips * cost_per_sled_dog_trip + truck_trips * cost_per_truck_trip <= budget)
    
    # Constraint: Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips)

    # Solve the problem
    solver.Solve()

    # Print the solution
    print('Number of sled dog trips:', sled_dog_trips.solution_value())
    print('Number of truck trips:', truck_trips.solution_value())
    print('Maximum fish transported:', objective.Value())

if __name__ == '__main__':
    maximize_fish_transport()
