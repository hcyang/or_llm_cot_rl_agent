from ortools.linear_solver import pywraplp

def max_fish_transport(sled_capacity, truck_capacity, sled_cost, truck_cost, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        print("Solver not created.")
        return None

    # Define decision variables
    # Number of sled dog trips
    sled_trips = solver.NumVar(0, solver.infinity(), 'sled_trips')
    # Number of truck trips
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Define the objective function: maximize fish transported
    solver.Maximize(sled_capacity * sled_trips + truck_capacity * truck_trips)

    # Define the constraints
    # Budget constraint
    solver.Add(sled_cost * sled_trips + truck_cost * truck_trips <= budget)

    # Constraint: sled trips must be less than truck trips
    solver.Add(sled_trips < truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution found!")
        print(f"Number of sled dog trips: {sled_trips.solution_value()}")
        print(f"Number of truck trips: {truck_trips.solution_value()}")
        print(f"Maximum number of fish transported: {solver.Objective().Value()}")
        return solver.Objective().Value()
    else:
        print("No optimal solution found.")
        return None

# Example usage
sled_capacity = 500   # Amount of fish sled dogs can transport per trip
truck_capacity = 2000 # Amount of fish trucks can transport per trip
sled_cost = 100       # Cost per sled dog trip
truck_cost = 500      # Cost per truck trip
budget = 10000        # Budget limit

max_fish_transport(sled_capacity, truck_capacity, sled_cost, truck_cost, budget)
