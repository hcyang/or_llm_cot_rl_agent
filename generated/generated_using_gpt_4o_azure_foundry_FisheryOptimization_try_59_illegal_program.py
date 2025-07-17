from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_s, F_t, C_s, C_t, B):
    # Create the linear solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Define the variables for the number of sled dog trips and truck trips
    x = solver.IntVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # truck trips
    
    # Define the constraints
    solver.Add(C_s * x + C_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips
    
    # Define the objective function
    solver.Maximize(F_s * x + F_t * y)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips (x):', x.solution_value())
        print('Number of truck trips (y):', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage:
F_s = 50  # Number of fish per sled dog trip
F_t = 100  # Number of fish per truck trip
C_s = 20  # Cost per sled dog trip
C_t = 40  # Cost per truck trip
B = 1000  # Total budget

maximize_fish_transport(F_s, F_t, C_s, C_t, B)
