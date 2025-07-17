from ortools.linear_solver import pywraplp

def solve_fish_transportation():
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('SCIP solver unavailable.')
        return

    # Variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Cost constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)

    # Sled dog trips must be less than truck trips
    # Equivalent to: sled_dog_trips <= truck_trips - 1
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('OBJECTIVE=', solver.Objective().Value())
        print('Number of sled dog trips:', sled_dog_trips.solution_value())
        print('Number of truck trips:', truck_trips.solution_value())
    else:
        print('The problem does not have an optimal solution.')

solve_fish_transportation()
