from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    solver.Add(sled_dog_trips <= truck_trips - 1)  # sled dog trips must be less than truck trips
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)  # Budget constraint

    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Sled dog trips:', sled_dog_trips.solution_value())
        print('Truck trips:', truck_trips.solution_value())
        print('Total fish transported:', 100 * sled_dog_trips.solution_value() + 200 * truck_trips.solution_value())
        print('OBJECTIVE=', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
