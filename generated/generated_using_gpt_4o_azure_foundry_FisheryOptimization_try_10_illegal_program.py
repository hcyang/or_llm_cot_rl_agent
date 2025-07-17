from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled_trip, fish_per_truck_trip, cost_per_sled_trip, cost_per_truck_trip, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips

    # Define the constraints
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget)
    solver.Add(x < y)

    # Define the objective function
    solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters
fish_per_sled_trip = 50
fish_per_truck_trip = 200
cost_per_sled_trip = 100
cost_per_truck_trip = 300
budget = 5000

maximize_fish_transport(fish_per_sled_trip, fish_per_truck_trip, cost_per_sled_trip, cost_per_truck_trip, budget)
