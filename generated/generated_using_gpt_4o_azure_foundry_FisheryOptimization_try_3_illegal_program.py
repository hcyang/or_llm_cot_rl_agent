from ortools.linear_solver import pywraplp

def max_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Define the decision variables
    # x: number of sled dog trips
    # y: number of truck trips
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Coefficients for fish transported per trip
    fish_per_sled_trip = 50  # Example value
    fish_per_truck_trip = 200  # Example value

    # Cost per trip
    cost_per_sled_trip = 100  # Example value
    cost_per_truck_trip = 300  # Example value

    # Budget constraint
    budget = 5000  # Example budget

    # Constraint: x < y
    solver.Add(x < y)

    # Constraint: Cost within budget
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget)

    # Objective: Maximize fish transported
    objective = solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Solve the problem
    solver.Solve()

    # Print the solution
    num_sled_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish = fish_per_sled_trip * num_sled_trips + fish_per_truck_trip * num_truck_trips

    print(f'Number of sled dog trips: {num_sled_trips}')
    print(f'Number of truck trips: {num_truck_trips}')
    print(f'Maximum number of fish transported: {max_fish}')

    return max_fish

# Run the function
max_fish_transport()
