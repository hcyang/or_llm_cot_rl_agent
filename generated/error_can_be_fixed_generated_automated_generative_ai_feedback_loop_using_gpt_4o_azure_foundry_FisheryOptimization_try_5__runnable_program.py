from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        print('Solver not created.')
        return

    # Parameters
    fish_per_sled_dog_trip = 10
    fish_per_truck_trip = 25
    cost_per_sled_dog_trip = 20
    cost_per_truck_trip = 50
    budget = 500

    # Decision variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Auxiliary variable to handle strict inequality
    epsilon = solver.NumVar(0, solver.infinity(), 'epsilon')

    # Objective: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, fish_per_sled_dog_trip)
    objective.SetCoefficient(truck_trips, fish_per_truck_trip)
    objective.SetMaximization()

    # Constraints
    # Budget constraint
    solver.Add(cost_per_sled_dog_trip * sled_dog_trips + cost_per_truck_trip * truck_trips <= budget)

    # Constraint: sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips + epsilon <= truck_trips)

    # Solve the problem
    solver.Solve()

    # Print solution
    print('OBJECTIVE=', objective.Value())
    print('Number of sled dog trips:', sled_dog_trips.solution_value())
    print('Number of truck trips:', truck_trips.solution_value())

if __name__ == '__main__':
    main()
