from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        print("Solver not created.")
        return
    
    # Variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')
    
    # Constraints
    # 1. Budget constraint
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # 2. Number of sled dog trips must be less than number of truck trips
    # Using a workaround as direct < is not supported
    solver.Add(sled_dog_trips <= truck_trips - 1)
    
    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Truck trips: {truck_trips.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
