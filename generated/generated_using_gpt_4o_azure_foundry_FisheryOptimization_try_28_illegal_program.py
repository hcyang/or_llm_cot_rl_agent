from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        return None

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Define the constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value (maximum number of fish):', solver.Objective().Value())
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 80   # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
