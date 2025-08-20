from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("SCIP solver unavailable.")
        return

    # Decision variables
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
        sled_dog_trips * fish_per_sled_dog_trip +
        truck_trips * fish_per_truck_trip
    )

    # Constraints
    # 1. Total cost must be within the budget
    solver.Add(
        sled_dog_trips * cost_per_sled_dog_trip +
        truck_trips * cost_per_truck_trip <= budget_limit
    )

    # 2. The number of sled dog trips must be less than or equal to the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Display the results
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE={solver.Objective().Value()}')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    maximize_fish_transport()
