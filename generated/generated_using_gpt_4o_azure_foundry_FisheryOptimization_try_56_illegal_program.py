from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c1, c2, budget):
    # Create the solver instance
    solver = pywraplp.Solver.CreateSolver('GLOP')

    if not solver:
        return "Solver not created."

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Define the constraints
    # Cost constraint
    solver.Add(c1 * x + c2 * y <= budget)

    # Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Solve the problem
    status = solver.Solve()

    # Check the result
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
a = 100  # number of fish per sled dog trip
b = 200  # number of fish per truck trip
c1 = 50  # cost per sled dog trip
c2 = 80  # cost per truck trip
budget = 1000  # total budget

maximize_fish_transport(a, b, c1, c2, budget)
