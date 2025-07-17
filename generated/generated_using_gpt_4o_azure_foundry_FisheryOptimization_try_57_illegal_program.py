from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c1, c2, budget):
    # Create the solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        return None

    # Decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips

    # Constraints
    solver.Add(c1 * x + c2 * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Number of trips constraint

    # Objective function
    solver.Maximize(a * x + b * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return {
            'objective_value': solver.Objective().Value(),
            'sled_dog_trips': x.solution_value(),
            'truck_trips': y.solution_value()
        }
    else:
        return None

# Example usage
a = 100  # Number of fish per sled dog trip
b = 200  # Number of fish per truck trip
c1 = 50  # Cost per sled dog trip
c2 = 100 # Cost per truck trip
budget = 1000  # Total budget

solution = maximize_fish_transport(a, b, c1, c2, budget)
if solution:
    print(f"Objective value (max fish): {solution['objective_value']}")
    print(f"Sled dog trips: {solution['sled_dog_trips']}")
    print(f"Truck trips: {solution['truck_trips']}")
else:
    print("No solution found.")
