from ortools.linear_solver import pywraplp

def transport_fish_maximize(fish_per_sled_trip, fish_per_truck_trip, 
                            cost_per_sled_trip, cost_per_truck_trip, budget_limit):
    # Create the linear solver with the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        print("Solver not found.")
        return

    # Decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Objective function: Maximize total fish transported
    solver.Maximize(fish_per_sled_trip * x + fish_per_truck_trip * y)

    # Constraints
    # Budget constraint
    solver.Add(cost_per_sled_trip * x + cost_per_truck_trip * y <= budget_limit)
    
    # Sled dog trips must be less than truck trips
    solver.Add(x <= y - 1)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal solution found:')
        print(f'Number of sled dog trips (x): {x.solution_value()}')
        print(f'Number of truck trips (y): {y.solution_value()}')
        print(f'Total fish transported: {solver.Objective().Value()}')
    else:
        print('No optimal solution found.')

# Example input
fish_per_sled_trip = 100
fish_per_truck_trip = 200
cost_per_sled_trip = 50
cost_per_truck_trip = 100
budget_limit = 1000

transport_fish_maximize(fish_per_sled_trip, fish_per_truck_trip, 
                        cost_per_sled_trip, cost_per_truck_trip, budget_limit)
