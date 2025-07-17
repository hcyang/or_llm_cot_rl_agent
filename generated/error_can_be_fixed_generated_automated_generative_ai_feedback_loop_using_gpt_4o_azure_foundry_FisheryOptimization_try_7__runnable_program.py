from ortools.linear_solver import pywraplp

def main():
    # Create the solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("SCIP solver unavailable.")
        return

    # Parameters
    fish_per_trip_dog = 100  # Amount of fish a sled dog can transport per trip
    cost_per_trip_dog = 50   # Cost per sled dog trip
    fish_per_trip_truck = 200  # Amount of fish a truck can transport per trip
    cost_per_trip_truck = 100  # Cost per truck trip
    budget = 1000  # Total budget available

    # Variables
    num_trips_dog = solver.IntVar(0, solver.infinity(), 'num_trips_dog')
    num_trips_truck = solver.IntVar(0, solver.infinity(), 'num_trips_truck')

    # Constraints
    # Total cost must not exceed the budget
    solver.Add(cost_per_trip_dog * num_trips_dog + cost_per_trip_truck * num_trips_truck <= budget)

    # Number of sled dog trips must be less than the number of truck trips
    # Use an auxiliary variable to model the strict inequality
    epsilon = 1
    solver.Add(num_trips_dog + epsilon <= num_trips_truck)

    # Objective: Maximize the number of fish transported
    objective = solver.Maximize(fish_per_trip_dog * num_trips_dog + fish_per_trip_truck * num_trips_truck)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('OBJECTIVE=', solver.Objective().Value())
        print('Number of sled dog trips:', num_trips_dog.solution_value())
        print('Number of truck trips:', num_trips_truck.solution_value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
