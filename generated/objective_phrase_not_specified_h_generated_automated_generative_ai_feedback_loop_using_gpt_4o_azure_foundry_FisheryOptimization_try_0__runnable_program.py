from ortools.linear_solver import pywraplp

def main():
    # Create the solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Constants
    fish_per_sled_dog_trip = 50  # Amount of fish sled dogs can carry per trip
    fish_per_truck_trip = 200    # Amount of fish trucks can carry per trip
    cost_per_sled_dog_trip = 100 # Cost per trip for sled dogs
    cost_per_truck_trip = 300    # Cost per trip for trucks
    budget = 5000                # Total budget available

    # Variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Cost constraint: total cost must not exceed the budget
    solver.Add(cost_per_sled_dog_trip * sled_dog_trips +
               cost_per_truck_trip * truck_trips <= budget)

    # The number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the total amount of fish transported
    solver.Maximize(fish_per_sled_dog_trip * sled_dog_trips +
                    fish_per_truck_trip * truck_trips)

    # Solve the problem
    solver.Solve()

    # Print the solution
    print('Solution:')
    print('Number of sled dog trips =', sled_dog_trips.solution_value())
    print('Number of truck trips =', truck_trips.solution_value())
    print('Total fish transported =', solver.Objective().Value())
    print('Objective score (maximized fish transported) =', solver.Objective().Value())

if __name__ == '__main__':
    main()
