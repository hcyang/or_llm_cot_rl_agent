from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the GLOP backend, which is suitable for linear programming problems.
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    if not solver:
        print("Solver not created.")
        return
    
    # Variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')
    
    # Objective function: Maximize the number of fish transported
    objective = solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)
    
    # Constraints
    # Budget constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # Constraint: The number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips < truck_trips)
    
    # Solve the problem
    solver.Solve()
    
    # Print the solution
    print('Number of sled dog trips:', sled_dog_trips.solution_value())
    print('Number of truck trips:', truck_trips.solution_value())
    print('Total fish transported:', 100 * sled_dog_trips.solution_value() + 200 * truck_trips.solution_value())
    print('OBJECTIVE=', solver.Objective().Value())

maximize_fish_transport()
