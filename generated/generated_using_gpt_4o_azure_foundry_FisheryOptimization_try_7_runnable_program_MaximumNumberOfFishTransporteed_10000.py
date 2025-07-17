from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c1, c2, B):
    # Create the solver instance
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Define the constraints
    solver.Add(c1 * x + c2 * y <= B)  # Cost constraint
    solver.Add(x <= y - 1)            # Number of trips constraint

    # Solve the problem
    status = solver.Solve()

    # Check the result status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c1 = 10  # Cost per sled dog trip
c2 = 20  # Cost per truck trip
B = 1000 # Total budget

maximize_fish_transport(a, b, c1, c2, B)
