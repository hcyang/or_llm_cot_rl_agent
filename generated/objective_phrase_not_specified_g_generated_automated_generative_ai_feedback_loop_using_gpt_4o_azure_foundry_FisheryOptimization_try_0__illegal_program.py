from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled_trip, fish_per_truck_trip,
                            cost_per_sled_trip, cost_per_truck_trip, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Objective: Maximize total fish transported
    solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Constraints
    # 1. Total cost does not exceed the budget
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget)

    # 2. Number of sled dog trips must be less than the number of truck trips
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum fish transported =', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example data
fish_per_sled_trip = 100   # Amount of fish transported per sled trip
fish_per_truck_trip = 500  # Amount of fish transported per truck trip
cost_per_sled_trip = 50    # Cost of one sled trip
cost_per_truck_trip = 150  # Cost of one truck trip
budget = 1000              # Total budget

maximize_fish_transport(fish_per_sled_trip, fish_per_truck_trip,
                        cost_per_sled_trip, cost_per_truck_trip, budget)
