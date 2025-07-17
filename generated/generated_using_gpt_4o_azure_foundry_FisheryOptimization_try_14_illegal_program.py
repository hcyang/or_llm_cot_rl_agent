from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Add the constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)  # sled dog trips less than truck trips

    # Solve the problem
    status = solver.Solve()

    # Check the result and return the solution
    if status == pywraplp.Solver.OPTIMAL:
        return {
            'objective_value': solver.Objective().Value(),
            'sled_dog_trips': x.solution_value(),
            'truck_trips': y.solution_value()
        }
    else:
        return None

# Example usage:
a = 10  # fish per sled dog trip
b = 20  # fish per truck trip
c = 100  # cost per sled dog trip
d = 150  # cost per truck trip
budget = 1000  # total budget

result = maximize_fish_transport(a, b, c, d, budget)
if result:
    print(f"Objective value (total fish): {result['objective_value']}")
    print(f"Sled dog trips: {result['sled_dog_trips']}")
    print(f"Truck trips: {result['truck_trips']}")
else:
    print("No optimal solution found.")
