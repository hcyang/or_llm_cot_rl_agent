from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not found.")
        return

    # Define decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define parameters
    sled_dog_capacity = 100  # Fish per sled dog trip
    truck_capacity = 200     # Fish per truck trip
    sled_dog_cost = 10       # Cost per sled dog trip
    truck_cost = 30          # Cost per truck trip
    budget_limit = 100       # Total cost budget

    # Objective function: Maximize the total number of fish transported
    solver.Maximize(sled_dog_trips * sled_dog_capacity + truck_trips * truck_capacity)

    # Constraints
    # 1. Total cost must not exceed the budget
    solver.Add(sled_dog_trips * sled_dog_cost + truck_trips * truck_cost <= budget_limit)

    # 2. The number of sled dog trips must be less than the number of truck trips
    # Since strict inequalities are not allowed, we reformulate as sled_dog_trips + 1 <= truck_trips
    solver.Add(sled_dog_trips + 1 <= truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE={solver.Objective().Value()}')
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# Run the program
maximize_fish_transport()
