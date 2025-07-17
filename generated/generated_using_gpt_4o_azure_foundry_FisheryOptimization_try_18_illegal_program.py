from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled_trip, fish_per_truck_trip, 
                            cost_per_sled_trip, cost_per_truck_trip, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    # 1. Budget constraint
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget)

    # 2. Trip constraint
    solver.Add(x < y)

    # Define the objective function
    # Maximize the number of fish transported
    solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Solve the problem
    solver.Solve()

    # Get the results
    num_sled_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    objective_value = solver.Objective().Value()

    return num_sled_trips, num_truck_trips, objective_value

# Example values
fish_per_sled_trip = 100
fish_per_truck_trip = 500
cost_per_sled_trip = 50
cost_per_truck_trip = 200
budget = 1000

# Get the solution
num_sled_trips, num_truck_trips, objective_value = maximize_fish_transport(
    fish_per_sled_trip, fish_per_truck_trip, cost_per_sled_trip, cost_per_truck_trip, budget)

print(f'Number of sled dog trips: {num_sled_trips}')
print(f'Number of truck trips: {num_truck_trips}')
print(f'Maximum number of fish transported: {objective_value}')
