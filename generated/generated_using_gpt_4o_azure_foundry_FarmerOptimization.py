from ortools.linear_solver import pywraplp

def maximize_profit(L, F, P, F1, P1, S1, F2, P2, S2):
    # Create the linear solver with the SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Variables
    x1 = solver.NumVar(0, solver.infinity(), 'x1')  # hectares of wheat
    x2 = solver.NumVar(0, solver.infinity(), 'x2')  # hectares of barley

    # Constraints
    solver.Add(x1 + x2 <= L)  # Land constraint
    solver.Add(F1 * x1 + F2 * x2 <= F)  # Fertilizer constraint
    solver.Add(P1 * x1 + P2 * x2 <= P)  # Pesticide constraint

    # Objective function
    solver.Maximize(S1 * x1 + S2 * x2)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print(f'Wheat (x1) hectares = {x1.solution_value()}')
        print(f'Barley (x2) hectares = {x2.solution_value()}')
        print(f'Maximized profit = {solver.Objective().Value()}')
    else:
        print('The problem does not have an optimal solution.')

# Example values
L = 100  # Total land in hectares
F = 500  # Total fertilizer in kilograms
P = 300  # Total pesticide in kilograms
F1 = 5   # Fertilizer required per hectare of wheat
P1 = 2   # Pesticide required per hectare of wheat
S1 = 100 # Selling price per hectare of wheat
F2 = 4   # Fertilizer required per hectare of barley
P2 = 3   # Pesticide required per hectare of barley
S2 = 150 # Selling price per hectare of barley

maximize_profit(L, F, P, F1, P1, S1, F2, P2, S2)
