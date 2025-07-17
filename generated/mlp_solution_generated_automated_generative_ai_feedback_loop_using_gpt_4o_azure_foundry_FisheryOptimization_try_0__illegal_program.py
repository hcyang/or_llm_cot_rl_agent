from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        print('Solver not found.')
        return

    # Define decision variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define the constraints
    # Cost constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)

    # Number of sled dog trips must be less than the number of truck trips
    solver.Add(sled_dog_trips < truck_trips)

    # Define the objective function: Maximize fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value:', solver.Objective().Value())
        print(f'Sled Dog Trips: {sled_dog_trips.solution_value()}')
        print(f'Truck Trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
