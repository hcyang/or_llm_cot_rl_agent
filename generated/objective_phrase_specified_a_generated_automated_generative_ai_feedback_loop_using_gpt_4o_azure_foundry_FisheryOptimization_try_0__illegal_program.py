from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        raise Exception("Solver not found.")

    # Define variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Define constraints
    solver.Add(c * x + d * y <= budget)
    solver.Add(x < y)

    # Define the objective
    objective = solver.Maximize(a * x + b * y)

    # Solve the problem
    solver.Solve()

    # Get the results
    num_sled_dog_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish_transported = a * num_sled_dog_trips + b * num_truck_trips

    print(f"OBJECTIVE={max_fish_transported}")
    print(f"Number of sled dog trips: {num_sled_dog_trips}")
    print(f"Number of truck trips: {num_truck_trips}")

# Example usage
a = 10  # amount of fish per sled dog trip
b = 20  # amount of fish per truck trip
c = 5   # cost per sled dog trip
d = 10  # cost per truck trip
budget = 100  # budget limit

maximize_fish_transport(a, b, c, d, budget)
