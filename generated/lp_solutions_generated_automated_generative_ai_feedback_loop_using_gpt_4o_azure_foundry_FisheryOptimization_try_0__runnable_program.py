from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the GLOP backend, which is suitable for linear programming.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables for the number of sled dog trips and truck trips.
    sled_dog_trips = solver.NumVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.NumVar(0, solver.infinity(), 'truck_trips')

    # Define the objective function: maximize the number of fish transported.
    solver.Maximize(100 * sled_dog_trips + 200 * truck_trips)

    # Add the budget constraint: cost of sled dog trips and truck trips must be less than or equal to 100.
    solver.Add(10 * sled_dog_trips + 30 * truck_trips <= 100)

    # Add the constraint that the number of sled dog trips must be less than the number of truck trips.
    solver.Add(sled_dog_trips <= truck_trips)

    # Solve the problem.
    status = solver.Solve()

    # Check the result status.
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Number of sled dog trips: {sled_dog_trips.solution_value()}')
        print(f'Number of truck trips: {truck_trips.solution_value()}')
        print(f'OBJECTIVE= {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

maximize_fish_transport()
