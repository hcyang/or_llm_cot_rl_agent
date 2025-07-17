from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        print("Solver not found.")
        return

    # Variables
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Constraints
    # Constraint 1: Cost constraint
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)
    
    # Constraint 2: Sled dog trips must be less than truck trips
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Objective: Maximize the number of fish transported
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Sled dog trips:', sled_dog_trips.solution_value())
        print('Truck trips:', truck_trips.solution_value())
        print('Objective value:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
