from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget):
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # 1. Cost constraint: The total cost must not exceed the budget.
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)

    # 2. Sled dog trips must be less than truck trips.
    solver.Add(sled_dog_trips < truck_trips)

    # Objective function: Maximize the total number of fish transported.
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', sled_dog_trips.solution_value())
        print('Number of truck trips:', truck_trips.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
sled_dog_capacity = 100  # Fish per sled dog trip
sled_dog_cost = 50       # Cost per sled dog trip
truck_capacity = 300     # Fish per truck trip
truck_cost = 150         # Cost per truck trip
budget = 1000            # Total budget

maximize_fish_transport(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget)
