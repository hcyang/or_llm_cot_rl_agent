from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function: Maximize a*x + b*y
    solver.Maximize(a * x + b * y)

    # Define the constraints
    # Cost constraint: c*x + d*y <= budget
    solver.Add(c * x + d * y <= budget)

    # Sled dog trips less than truck trips: x < y
    solver.Add(x <= y - 1)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        return {
            'objective_value': solver.Objective().Value(),
            'sled_dog_trips': x.solution_value(),
            'truck_trips': y.solution_value()
        }
    else:
        return None

# Example values
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 80   # Cost per truck trip
budget = 1000  # Total budget

result = maximize_fish_transport(a, b, c, d, budget)
if result:
    print(f"Objective Value (Total Fish): {result['objective_value']}")
    print(f"Sled Dog Trips: {result['sled_dog_trips']}")
    print(f"Truck Trips: {result['truck_trips']}")
else:
    print("No optimal solution found.")
