from ortools.linear_solver import pywraplp

def main():
    # Create the linear solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        print("Solver not created.")
        return

    # Variables
    # Number of trips by sled dogs
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    # Number of trips by trucks
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Cost constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)

    # Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
