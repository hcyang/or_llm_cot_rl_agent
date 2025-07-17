from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    if not solver:
        print("Solver not created.")
        return

    # Decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # truck trips

    # Objective function: maximize a * x + b * y
    solver.Maximize(a * x + b * y)

    # Constraints
    # Cost constraint: c * x + d * y <= budget
    solver.Add(c * x + d * y <= budget)
    
    # Sled dog trips must be less than truck trips: x < y
    solver.Add(x < y)

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value:', solver.Objective().Value())
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 300  # Cost per sled dog trip
d = 500  # Cost per truck trip
budget = 5000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
