from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_s, f_t, c_s, c_t, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips
    
    # Constraints
    solver.Add(c_s * x + c_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips
    
    # Objective
    solver.Maximize(f_s * x + f_t * y)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters (you can change these to your specific problem)
f_s = 100  # Example number of fish per sled dog trip
f_t = 300  # Example number of fish per truck trip
c_s = 50   # Example cost per sled dog trip
c_t = 150  # Example cost per truck trip
B = 1000   # Example total budget

maximize_fish_transport(f_s, f_t, c_s, c_t, B)
