from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using GLOP (Google Linear Optimization Package)
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Define variables
    sled_dogs_trips = solver.IntVar(0, solver.infinity(), 'sled_dogs_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define coefficients
    fish_per_sled_dogs_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dogs_trip = 10
    cost_per_truck_trip = 30
    budget_limit = 100

    # Define the objective function: Maximize the total number of fish transported
    solver.Maximize(sled_dogs_trips * fish_per_sled_dogs_trip +
                    truck_trips * fish_per_truck_trip)

    # Define the budget constraint
    solver.Add(sled_dogs_trips * cost_per_sled_dogs_trip +
               truck_trips * cost_per_truck_trip <= budget_limit)

    # Define the constraint: number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dogs_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    # Check the result status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Sled Dogs Trips: {sled_dogs_trips.solution_value()}')
        print(f'Truck Trips: {truck_trips.solution_value()}')
        print(f'OBJECTIVE= {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Run the function
maximize_fish_transport()
