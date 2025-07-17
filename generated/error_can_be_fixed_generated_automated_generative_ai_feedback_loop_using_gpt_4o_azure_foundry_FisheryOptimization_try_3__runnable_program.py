from ortools.linear_solver import pywraplp

def main():
    # Instantiate a Glop solver, which is a linear programming solver.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Constants
    fish_per_sled_trip = 10  # Amount of fish a sled can transport per trip
    fish_per_truck_trip = 50  # Amount of fish a truck can transport per trip
    cost_per_sled_trip = 5  # Cost per sled trip
    cost_per_truck_trip = 20  # Cost per truck trip
    budget = 500  # Total budget

    # Decision variables
    sled_trips = solver.NumVar(0, solver.infinity(), 'sled_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Objective: Maximize the number of fish transported
    solver.Maximize(fish_per_sled_trip * sled_trips + fish_per_truck_trip * truck_trips)

    # Constraints
    # Budget constraint
    solver.Add(cost_per_sled_trip * sled_trips + cost_per_truck_trip * truck_trips <= budget)

    # Sled trips must be less than truck trips
    solver.Add(sled_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Solution: Sled Trips = {sled_trips.solution_value()}, Truck Trips = {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
