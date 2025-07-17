from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables for sled dog and truck trips
    x = solver.IntVar(0, solver.infinity(), 'x')
    y = solver.IntVar(0, solver.infinity(), 'y')

    # Define the coefficients
    a = 100  # fish per sled dog trip
    b = 400  # fish per truck trip
    c = 50   # cost per sled dog trip
    d = 200  # cost per truck trip
    budget = 4000

    # Define the constraints
    solver.Add(c * x + d * y <= budget)  # cost constraint
    solver.Add(x < y)                    # sled dog trips must be less than truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    maximize_fish_transport()
