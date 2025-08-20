from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return "Solver not created."
    
    # Define decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')
    
    # Fish transported per trip
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    
    # Cost per trip
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    
    # Budget constraint
    budget_limit = 100
    
    # Objective: Maximize fish transported
    solver.Maximize(
        fish_per_sled_dog_trip * sled_dog_trips +
        fish_per_truck_trip * truck_trips
    )
    
    # Add constraints
    solver.Add(
        cost_per_sled_dog_trip * sled_dog_trips +
        cost_per_truck_trip * truck_trips <= budget_limit
    )
    
    # Constraint: Number of sled dog trips < Number of truck trips
    solver.Add(sled_dog_trips + 1 <= truck_trips)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print("Solution Found!")
        print(f"Number of sled dog trips: {sled_dog_trips.solution_value()}")
        print(f"Number of truck trips: {truck_trips.solution_value()}")
        print(f"OBJECTIVE={solver.Objective().Value()}")
    else:
        print("The problem does not have an optimal solution.")

# Run the program
maximize_fish_transport()
