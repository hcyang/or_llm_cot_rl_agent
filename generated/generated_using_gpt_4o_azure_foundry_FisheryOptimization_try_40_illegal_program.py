from ortools.linear_solver import pywraplp

def maximize_fish_transport(sled_dogs_capacity, truck_capacity, sled_dogs_cost, truck_cost, budget):
    # Create the linear solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Solver not created.")
        return

    # Decision variables
    sled_dogs_trips = solver.IntVar(0, solver.infinity(), 'sled_dogs_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Objective function: Maximize the number of fish transported
    solver.Maximize(sled_dogs_capacity * sled_dogs_trips + truck_capacity * truck_trips)

    # Constraints
    # Budget constraint
    solver.Add(sled_dogs_cost * sled_dogs_trips + truck_cost * truck_trips <= budget)
    
    # Sled dogs trips must be less than truck trips
    solver.Add(sled_dogs_trips < truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Number of sled dogs trips:", sled_dogs_trips.solution_value())
        print("Number of truck trips:", truck_trips.solution_value())
        print("Maximum number of fish transported:", solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print("The problem does not have an optimal solution.")
        return None

# Example values for capacities, costs, and budget
sled_dogs_capacity = 500  # Number of fish per sled dog trip
truck_capacity = 2000     # Number of fish per truck trip
sled_dogs_cost = 100      # Cost per sled dog trip
truck_cost = 500          # Cost per truck trip
budget = 5000             # Total budget

maximize_fish_transport(sled_dogs_capacity, truck_capacity, sled_dogs_cost, truck_cost, budget)
