from ortools.linear_solver import pywraplp

def solve_fishery_transportation(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    if not solver:
        print("Solver not created.")
        return None
    
    # Variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)
    
    # Constraints
    # 1. Total cost should be within budget
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)
    
    # 2. The number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
sled_dog_capacity = 100  # Example: Sled dogs can transport 100 fish per trip
truck_capacity = 500     # Example: Trucks can transport 500 fish per trip
sled_dog_cost = 50       # Example: Cost per sled dog trip
truck_cost = 200         # Example: Cost per truck trip
budget = 1000            # Example: Total budget

solve_fishery_transportation(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget)
