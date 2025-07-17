from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the GLOP backend (Google's Linear Optimization Package)
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Define variables
    # Let x be the number of sled dog trips
    # Let y be the number of truck trips
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    # Constants
    fish_per_sled_dog_trip = 100  # The amount of fish transported by sled dogs per trip
    fish_per_truck_trip = 500     # The amount of fish transported by trucks per trip
    cost_per_sled_dog_trip = 50   # Cost per sled dog trip
    cost_per_truck_trip = 200     # Cost per truck trip
    budget_limit = 2000           # Total budget

    # Objective function: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(x, fish_per_sled_dog_trip)
    objective.SetCoefficient(y, fish_per_truck_trip)
    objective.SetMaximization()

    # Constraints
    # 1. Budget constraint: Total cost must not exceed the budget limit
    solver.Add(cost_per_sled_dog_trip * x + cost_per_truck_trip * y <= budget_limit)

    # 2. Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Solve the problem
    solver.Solve()

    # Get the results
    num_sled_dog_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    objective_value = solver.Objective().Value()

    # Display the solution
    print(f"Number of sled dog trips: {num_sled_dog_trips}")
    print(f"Number of truck trips: {num_truck_trips}")
    print(f"OBJECTIVE= {objective_value}")

# Call the function to solve the problem
maximize_fish_transport()
