from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the linear solver with the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function: Maximize a*x + b*y
    solver.Maximize(a * x + b * y)

    # Define the constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)                    # Sled dog trips < Truck trips

    # Solve the problem
    status = solver.Solve()

    # Check if the solution is optimal
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 300  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 200  # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
