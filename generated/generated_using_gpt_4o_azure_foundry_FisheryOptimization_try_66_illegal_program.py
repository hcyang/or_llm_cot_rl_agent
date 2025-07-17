from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None
    
    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')
    
    # Objective function: Maximize the number of fish transported
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)
    
    # Constraints
    # Total cost constraint
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)
    
    # Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips < truck_trips)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the solution status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('Sled dog trips =', sled_dog_trips.solution_value())
        print('Truck trips =', truck_trips.solution_value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
sled_dog_capacity = 100  # Number of fish per sled dog trip
sled_dog_cost = 50       # Cost per sled dog trip
truck_capacity = 500     # Number of fish per truck trip
truck_cost = 200         # Cost per truck trip
budget = 1000            # Total budget available

maximize_fish_transport(sled_dog_capacity, sled_dog_cost, truck_capacity, truck_cost, budget)
