from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Cost constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # Constraint: Number of sled dog trips must be less than the number of truck trips
    # Since "<" is not directly supported, we can rewrite it as:
    # sled_dog_trips <= truck_trips - 1
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    # 100 * sled_dog_trips + 200 * truck_trips
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check if the solution is optimal
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE={solver.Objective().Value()}')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
