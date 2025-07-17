
from ortools.linear_solver import pywraplp  
  
def maximize_profit(L, F, P, F1, P1, F2, P2, S1, S2):  
    # Create the linear solver using the GLOP backend.  
    solver = pywraplp.Solver.CreateSolver('GLOP')  
    if not solver:  
        print("Solver not available.")  
        return None  
  
    # Define the variables: x1 (land for wheat) and x2 (land for barley).  
    x1 = solver.NumVar(0, L, 'x1')  # Wheat area cannot exceed total land.  
    x2 = solver.NumVar(0, L, 'x2')  # Barley area cannot exceed total land.  
  
    # Define the constraints.  
    # Total land constraint: x1 + x2 <= L  
    solver.Add(x1 + x2 <= L)  
  
    # Fertilizer constraint: F1 * x1 + F2 * x2 <= F  
    solver.Add(F1 * x1 + F2 * x2 <= F)  
  
    # Pesticide constraint: P1 * x1 + P2 * x2 <= P  
    solver.Add(P1 * x1 + P2 * x2 <= P)  
  
    # Define the objective function: maximize profit.  
    profit = S1 * x1 + S2 * x2  
    solver.Maximize(profit)  
  
    # Solve the problem.  
    status = solver.Solve()  
  
    # Check the result.  
    if status == pywraplp.Solver.OPTIMAL:  
        print("Optimal solution found!")  
        print(f"Area planted with wheat (x1): {x1.solution_value()} hectares")  
        print(f"Area planted with barley (x2): {x2.solution_value()} hectares")  
        print(f"Maximum profit: {solver.Objective().Value()}")  
    else:  
        print("The solver could not find an optimal solution.")  
  
# Example usage:  
L = 100  # Total land available in hectares  
F = 1000  # Total fertilizer available in kilograms  
P = 500  # Total pesticide available in kilograms  
F1 = 10  # Fertilizer required per hectare of wheat  
P1 = 5   # Pesticide required per hectare of wheat  
F2 = 20  # Fertilizer required per hectare of barley  
P2 = 10  # Pesticide required per hectare of barley  
S1 = 200  # Selling price per hectare of wheat  
S2 = 150  # Selling price per hectare of barley  
  
maximize_profit(L, F, P, F1, P1, F2, P2, S1, S2)  

# Optimal solution found!
# Area planted with wheat (x1): 100.0 hectares
# Area planted with barley (x2): 1.665334536937735e-14 hectares
# Maximum profit: 20000.000000000004
