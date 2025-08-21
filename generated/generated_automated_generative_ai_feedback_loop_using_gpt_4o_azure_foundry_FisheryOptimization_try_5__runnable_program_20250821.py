from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("Solver not created. Make sure you have OR-Tools installed.")
        return
    
    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')  # Number of sled dog trips
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')        # Number of truck trips
    
    # Parameters
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    cost_budget = 100
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(
        fish_per_sled_dog_trip * sled_dog_trips +
        fish_per_truck_trip * truck_trips
    )
    
    # Constraints
    # Total cost constraint
    solver.Add(
        cost_per_sled_dog_trip * sled_dog_trips +
        cost_per_truck_trip * truck_trips <= cost_budget
    )
    
    # Sled dog trips must be less than truck trips
    # sled_dog_trips < truck_trips is equivalent to sled_dog_trips <= truck_trips - 1
    solver.Add(sled_dog_trips <= truck_trips - 1)
    
    # Solve the problem
    status = solver.Solve()
    
    # Check if the problem has an optimal solution
    if status == pywraplp.Solver.OPTIMAL:
        print(f"OBJECTIVE={solver.Objective().Value()}")
        print(f"Sled dog trips: {sled_dog_trips.solution_value()}")
        print(f"Truck trips: {truck_trips.solution_value()}")
    else:
        print("The solver did not find an optimal solution.")

# Call the function to solve the problem
maximize_fish_transport()
