from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_trip_sled, fish_per_trip_truck, cost_per_trip_sled, cost_per_trip_truck, budget):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips
    
    # Objective function
    solver.Maximize(fish_per_trip_sled * x + fish_per_trip_truck * y)
    
    # Constraints
    # Cost constraint
    solver.Add(cost_per_trip_sled * x + cost_per_trip_truck * y <= budget)
    
    # x < y
    solver.Add(x < y)
    
    # Solve the problem and check the result
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x):', x.solution_value())
        print('Number of truck trips (y):', y.solution_value())
        print('Objective value (maximum fish):', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
fish_per_trip_sled = 100
fish_per_trip_truck = 200
cost_per_trip_sled = 50
cost_per_trip_truck = 100
budget = 1000

maximize_fish_transport(fish_per_trip_sled, fish_per_trip_truck, cost_per_trip_sled, cost_per_trip_truck, budget)
