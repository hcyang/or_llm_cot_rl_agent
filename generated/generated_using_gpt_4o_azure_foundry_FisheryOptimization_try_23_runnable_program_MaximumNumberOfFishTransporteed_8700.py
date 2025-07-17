from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dogs_capacity, truck_capacity, sled_dogs_cost, truck_cost, budget):
    # Create the solver with the CBC backend.
    solver = pywraplp.Solver.CreateSolver('CBC')
    if not solver:
        return None

    # Variables
    sled_dogs_trips = solver.IntVar(0, solver.infinity(), 'sled_dogs_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Budget constraint
    solver.Add(sled_dogs_trips * sled_dogs_cost + truck_trips * truck_cost <= budget)
    
    # Sled dog trips must be less than truck trips
    solver.Add(sled_dogs_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    solver.Maximize(sled_dogs_trips * sled_dogs_capacity + truck_trips * truck_capacity)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', sled_dogs_trips.solution_value())
        print('Number of truck trips:', truck_trips.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
sled_dogs_capacity = 200  # Example capacity of fish per sled dog trip
truck_capacity = 500      # Example capacity of fish per truck trip
sled_dogs_cost = 100      # Example cost per sled dog trip
truck_cost = 300          # Example cost per truck trip
budget = 5000             # Example budget

maximize_fish_transport(sled_dogs_capacity, truck_capacity, sled_dogs_cost, truck_cost, budget)
