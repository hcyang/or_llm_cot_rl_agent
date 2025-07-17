from ortools.linear_solver import pywraplp

def maximize_fish_transportation(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not found.")
        return None

    # Define decision variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Define the objective function: Maximize the number of fish transported
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)

    # Define the constraints
    # Budget constraint: Total cost of trips should not exceed the budget
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)

    # Constraint: Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    # Check the result and print the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found:')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
sled_dog_capacity = 100  # Fish per sled dog trip
sled_dog_cost = 50       # Cost per sled dog trip
truck_capacity = 500     # Fish per truck trip
truck_cost = 300         # Cost per truck trip
budget = 3000            # Total budget

maximize_fish_transportation(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget)
