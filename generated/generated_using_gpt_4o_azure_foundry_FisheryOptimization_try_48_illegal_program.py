from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return 'Solver not created.'

    # Define variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Define the constraints
    # Budget constraint: c * x + d * y <= budget
    solver.Add(c * x + d * y <= budget)
    # x < y constraint
    solver.Add(x < y)

    # Define the objective function: Maximize a * x + b * y
    solver.Maximize(a * x + b * y)

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
        return 'The problem does not have an optimal solution.'

# Example usage with arbitrary values
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 80   # Cost per truck trip
budget = 1000  # Budget

solution = maximize_fish_transport(a, b, c, d, budget)
print(solution)
