from ortools.linear_solver import pywraplp

def maximize_fish_transportation(fish_per_sled_trip, fish_per_truck_trip,
                                 cost_per_sled_trip, cost_per_truck_trip,
                                 max_budget):
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables.
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function: Maximize fish transported.
    objective = solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Define the constraints.
    # 1. Total cost must be within budget.
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= max_budget)

    # 2. Number of sled dog trips must be less than the number of truck trips.
    solver.Add(x < y)

    # Solve the problem.
    solver.Solve()

    # Get the results.
    num_sled_dog_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    total_fish_transported = fish_per_sled_trip * num_sled_dog_trips + fish_per_truck_trip * num_truck_trips
    objective_value = solver.Objective().Value()

    print(f'Number of sled dog trips: {num_sled_dog_trips}')
    print(f'Number of truck trips: {num_truck_trips}')
    print(f'Total fish transported: {total_fish_transported}')
    print(f'OBJECTIVE= {objective_value}')

# Example usage
fish_per_sled_trip = 100
fish_per_truck_trip = 300
cost_per_sled_trip = 50
cost_per_truck_trip = 100
max_budget = 1000

maximize_fish_transportation(fish_per_sled_trip, fish_per_truck_trip,
                             cost_per_sled_trip, cost_per_truck_trip,
                             max_budget)
