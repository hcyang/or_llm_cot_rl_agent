from ortools.linear_solver import pywraplp

def solve_fish_transportation(f1, f2, c1, c2, B):
    # Create the linear solver with the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Constraints
    solver.Add(c1 * x + c2 * y <= B)  # Budget constraint
    solver.Add(x <= y - 1)            # Sled dog trips must be less than truck trips

    # Objective
    solver.Maximize(f1 * x + f2 * y)

    # Solve the problem
    status = solver.Solve()

    # Check if the problem has an optimal solution
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example usage with hypothetical data:
solve_fish_transportation(f1=10, f2=50, c1=100, c2=300, B=5000)
