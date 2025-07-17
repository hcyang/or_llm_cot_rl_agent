from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Define variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # truck trips
    
    # Define constraints
    solver.Add(c * x + d * y <= budget)  # Budget constraint
    solver.Add(x < y)                    # Sled dog trips less than truck trips
    
    # Define objective function
    solver.Maximize(a * x + b * y)
    
    # Solve the problem
    result_status = solver.Solve()
    
    # Check if the solution is optimal
    if result_status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('No optimal solution found.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 80   # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
