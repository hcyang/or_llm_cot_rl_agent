from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget):
    # Create the solver using the GLOP backend (Google Linear Optimization Package)
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define constraints
    # Budget constraint: sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget
    solver.Add(sled_dog_cost * sled_dog_trips + truck_cost * truck_trips <= budget)
    
    # Constraint: sled_dog_trips < truck_trips
    solver.Add(sled_dog_trips < truck_trips)

    # Define objective function: maximize sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips
    solver.Maximize(sled_dog_capacity * sled_dog_trips + truck_capacity * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check if the solution is optimal
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution is optimal:')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
        print(f'Maximum fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage
sled_dog_capacity = 100  # example capacity per sled dog trip
truck_capacity = 500     # example capacity per truck trip
sled_dog_cost = 50       # example cost per sled dog trip
truck_cost = 200         # example cost per truck trip
budget = 1000            # example budget

maximize_fish_transport(sled_dog_capacity, truck_capacity, sled_dog_cost, truck_cost, budget)
