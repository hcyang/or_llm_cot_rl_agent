from ortools.linear_solver import pywraplp

def solve_fish_transport_problem():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Parameters
    fish_per_trip_dogs = 100
    fish_per_trip_trucks = 200
    cost_per_trip_dogs = 50
    cost_per_trip_trucks = 100
    budget = 1000

    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Constraints
    solver.Add(cost_per_trip_dogs * x + cost_per_trip_trucks * y <= budget)
    solver.Add(x < y)

    # Objective
    solver.Maximize(fish_per_trip_dogs * x + fish_per_trip_trucks * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

solve_fish_transport_problem()
