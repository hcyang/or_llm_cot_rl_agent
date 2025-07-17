from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver using the GLOP backend, which is suitable for LP problems.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        print("Could not create solver.")
        return

    # Define the decision variables:
    # Let x be the number of sled dog trips.
    # Let y be the number of truck trips.
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    # Define the parameters of the problem:
    fish_per_sled_trip = 100  # Amount of fish transported per sled dog trip.
    fish_per_truck_trip = 200  # Amount of fish transported per truck trip.
    cost_per_sled_trip = 50    # Cost per sled dog trip.
    cost_per_truck_trip = 80   # Cost per truck trip.
    budget = 800               # Maximum budget available.

    # Define the objective function: Maximize the total number of fish transported.
    objective = solver.Objective()
    objective.SetCoefficient(x, fish_per_sled_trip)
    objective.SetCoefficient(y, fish_per_truck_trip)
    objective.SetMaximization()

    # Define the constraints:
    # Constraint 1: Total cost must not exceed the budget.
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget)

    # Constraint 2: Number of sled dog trips must be less than the number of truck trips.
    # We use a less-than-or-equal constraint by adding an auxiliary variable.
    solver.Add(x <= y - 1)

    # Solve the problem.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {objective.Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# Run the function
maximize_fish_transport()
