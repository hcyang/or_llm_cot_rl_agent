from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return None

    # Variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Objective: Maximize fish transported
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)

    # Constraints
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)
    solver.Add(sled_dog_trips < truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
        print(f'Maximized number of fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage with arbitrary values
sled_dog_capacity = 10  # Amount of fish sled dogs can transport per trip
truck_capacity = 50     # Amount of fish trucks can transport per trip
sled_dog_cost = 100     # Cost per sled dog trip
truck_cost = 500        # Cost per truck trip
budget = 5000           # Total budget available

maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget)
