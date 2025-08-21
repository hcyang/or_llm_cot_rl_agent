from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        print("Solver not available!")
        return
    
    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')
    
    # Constraints
    # 1. Cost budget upper limit
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # 2. Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips < truck_trips)
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)
    
    # Solve the problem
    status = solver.Solve()
    
    # Display results
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Sled dog trips: {sled_dog_trips.solution_value()}")
        print(f"Truck trips: {truck_trips.solution_value()}")
        print(f"OBJECTIVE={solver.Objective().Value()}")
    else:
        print("No optimal solution found.")

# Run the program
maximize_fish_transport()
