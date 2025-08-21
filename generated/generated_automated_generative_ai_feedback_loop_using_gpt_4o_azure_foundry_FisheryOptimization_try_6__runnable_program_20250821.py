from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not created. Please check your OR-Tools installation.")
        return

    # Variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Parameters
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    budget_limit = 100

    # Objective: Maximize the total number of fish transported
    solver.Maximize(
        fish_per_sled_dog_trip * sled_dog_trips +
        fish_per_truck_trip * truck_trips
    )

    # Constraints
    # 1. Cost constraint: The total cost must not exceed the budget
    solver.Add(
        cost_per_sled_dog_trip * sled_dog_trips +
        cost_per_truck_trip * truck_trips <= budget_limit
    )

    # 2. The number of sled dog trips must be strictly less than the number of truck trips
    # Reformulate the strict inequality (sled_dog_trips < truck_trips) as:
    # sled_dog_trips + 1 <= truck_trips
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

# Run the function
maximize_fish_transport()
