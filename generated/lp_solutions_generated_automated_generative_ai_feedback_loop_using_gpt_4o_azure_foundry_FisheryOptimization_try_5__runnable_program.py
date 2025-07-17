from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    sled_dogs_trips = solver.IntVar(0, solver.infinity(), 'sled_dogs_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define the constraints
    # Cost constraint: 10 * sled_dogs_trips + 30 * truck_trips <= 100
    solver.Add(10 * sled_dogs_trips + 30 * truck_trips <= 100)

    # Constraint: sled_dogs_trips must be less than truck_trips
    # This needs to be rewritten to be solver-friendly
    solver.Add(sled_dogs_trips <= truck_trips - 1)  # Equivalent to sled_dogs_trips < truck_trips

    # Define the objective function: Maximize fish transported
    objective = solver.Maximize(100 * sled_dogs_trips + 200 * truck_trips)

    # Solve the problem
    solver.Solve()

    # Print the solution
    print('OBJECTIVE=', solver.Objective().Value())
    print('Sled dogs trips:', sled_dogs_trips.solution_value())
    print('Truck trips:', truck_trips.solution_value())

if __name__ == '__main__':
    main()
