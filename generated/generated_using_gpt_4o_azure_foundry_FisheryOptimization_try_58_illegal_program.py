from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget_limit):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        return None

    # Decision variables: number of sled and truck trips.
    sled_trips = solver.IntVar(0, solver.infinity(), 'sled_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Objective: Maximize the number of fish transported.
    solver.Maximize(fish_per_sled * sled_trips + fish_per_truck * truck_trips)

    # Constraints:
    # Budget constraint.
    solver.Add(cost_per_sled * sled_trips + cost_per_truck * truck_trips <= budget_limit)
    # Sled trips less than truck trips constraint.
    solver.Add(sled_trips < truck_trips)

    # Solve the problem.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value: {solver.Objective().Value()}')
        print(f'Sled trips: {sled_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters
fish_per_sled = 100  # Example number of fish per sled trip
fish_per_truck = 500  # Example number of fish per truck trip
cost_per_sled = 20    # Example cost per sled trip
cost_per_truck = 50   # Example cost per truck trip
budget_limit = 1000   # Example budget limit

# Call the function
maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget_limit)
