from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Define the variables
    sled_dog_trips = solver.IntVar(0, solver.infinity(), 'sled_dog_trips')
    truck_trips = solver.IntVar(0, solver.infinity(), 'truck_trips')

    # Define the coefficients
    fish_per_sled_dog_trip = 100
    fish_per_truck_trip = 200
    cost_per_sled_dog_trip = 10
    cost_per_truck_trip = 30
    cost_budget = 100

    # Define the objective function: Maximize the total number of fish transported
    objective = solver.Maximize(fish_per_sled_dog_trip * sled_dog_trips +
                                fish_per_truck_trip * truck_trips)

    # Define the constraints
    # Cost constraint: 10 * sled_dog_trips + 30 * truck_trips <= 100
    solver.Add(cost_per_sled_dog_trip * sled_dog_trips +
               cost_per_truck_trip * truck_trips <= cost_budget)

    # Constraint to ensure sled dog trips are less than truck trips
    # We rewrite sled_dog_trips < truck_trips as sled_dog_trips <= truck_trips - 1
    solver.Add(sled_dog_trips <= truck_trips - 1)

    # Solve the problem
    status = solver.Solve()

    # Check the result status
    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value (max fish transported) =', 
              solver.Objective().Value())
        print('Sled dog trips =', sled_dog_trips.solution_value())
        print('Truck trips =', truck_trips.solution_value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
