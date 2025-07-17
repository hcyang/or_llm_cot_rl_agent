from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Parameters
    fish_per_trip_dogs = 200
    fish_per_trip_trucks = 500
    cost_per_trip_dogs = 100
    cost_per_trip_trucks = 300
    budget = 5000

    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Objective function: Maximize fish transported
    solver.Maximize(fish_per_trip_dogs * x + fish_per_trip_trucks * y)

    # Constraints
    solver.Add(cost_per_trip_dogs * x + cost_per_trip_trucks * y <= budget)
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

maximize_fish_transport()
