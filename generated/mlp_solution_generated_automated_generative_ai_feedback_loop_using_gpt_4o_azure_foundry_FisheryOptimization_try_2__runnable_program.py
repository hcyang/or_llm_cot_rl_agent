from ortools.linear_solver import pywraplp

def main():
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print('SCIP solver unavailable.')
        return

    # Variables
    # Number of sled dog trips
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    # Number of truck trips
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Cost constraint
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    # Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print('Number of sled dog trips:', sled_dog_trips.solution_value())
        print('Number of truck trips:', truck_trips.solution_value())
        print('OBJECTIVE=', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
