from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled_dog_trip, fish_per_truck_trip, 
                            cost_per_sled_dog_trip, cost_per_truck_trip, budget):
    # Create the linear solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    if not solver:
        print("Solver not found.")
        return
    
    # Create variables for the number of sled dog trips and truck trips
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')
    
    # Constraint: Budget
    solver.Add(sled_dog_trips * cost_per_sled_dog_trip + truck_trips * cost_per_truck_trip <= budget)
    
    # Constraint: Number of sled dog trips must be less than number of truck trips
    solver.Add(sled_dog_trips <= truck_trips)
    
    # Objective: Maximize the number of fish transported
    objective = solver.Maximize(sled_dog_trips * fish_per_sled_dog_trip + truck_trips * fish_per_truck_trip)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
        print(f'Maximum number of fish transported: {objective.Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage:
maximize_fish_transport(
    fish_per_sled_dog_trip=10,  # Example value: 10 fish per sled dog trip
    fish_per_truck_trip=25,     # Example value: 25 fish per truck trip
    cost_per_sled_dog_trip=100, # Example value: 100 currency units per sled dog trip
    cost_per_truck_trip=150,    # Example value: 150 currency units per truck trip
    budget=1000                 # Example budget
)
