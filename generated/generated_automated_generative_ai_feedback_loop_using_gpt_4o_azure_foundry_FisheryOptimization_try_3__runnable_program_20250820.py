from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not available.")
        return

    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Parameters
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    cost_budget = 100

    # Objective function: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(sled_dog_trips, fish_per_sled_dog_trip)
    objective.SetCoefficient(truck_trips, fish_per_truck_trip)
    objective.SetMaximization()

    # Constraints
    # 1. Cost constraint
    solver.Add(sled_dog_trips * cost_per_sled_dog_trip + truck_trips * cost_per_truck_trip <= cost_budget)

    # 2. Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE={objective.Value()}')
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    maximize_fish_transport()
