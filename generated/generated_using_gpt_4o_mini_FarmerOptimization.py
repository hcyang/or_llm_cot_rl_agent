from ortools.linear_solver import pywraplp  
  
def main():  
    # Parameters  
    L = 100  # Total land in hectares  
    F = 500  # Total fertilizer in kilograms  
    P = 300  # Total pesticide in kilograms  
  
    # Input requirements for wheat and barley per hectare  
    F1 = 10  # Fertilizer required per hectare of wheat  
    P1 = 5   # Pesticide required per hectare of wheat  
    F2 = 15  # Fertilizer required per hectare of barley  
    P2 = 10  # Pesticide required per hectare of barley  
  
    # Selling prices  
    S1 = 200  # Selling price per hectare of wheat  
    S2 = 250  # Selling price per hectare of barley  
  
    # Create the solver  
    solver = pywraplp.Solver.CreateSolver('GLOP')  
  
    # Decision variables  
    x1 = solver.NumVar(0, L, 'x1')  # Area planted with wheat  
    x2 = solver.NumVar(0, L, 'x2')  # Area planted with barley  
  
    # Constraints  
    solver.Add(x1 + x2 <= L)  # Total land constraint  
    solver.Add(F1 * x1 + F2 * x2 <= F)  # Fertilizer constraint  
    solver.Add(P1 * x1 + P2 * x2 <= P)  # Pesticide constraint  
  
    # Objective function: Maximize profit  
    profit = S1 * x1 + S2 * x2  
    solver.Maximize(profit)  
  
    # Solve the problem  
    status = solver.Solve()  
  
    # Check if the solution is optimal  
    if status == pywraplp.Solver.OPTIMAL:  
        print('Solution:')  
        print('Area planted with wheat (x1):', x1.solution_value(), 'hectares')  
        print('Area planted with barley (x2):', x2.solution_value(), 'hectares')  
        print('Maximum profit:', solver.Objective().Value())  
    else:  
        print('The problem does not have an optimal solution.')  
  
if __name__ == '__main__':  
    main()  


# Solution:
# Area planted with wheat (x1): 49.999999999999986 hectares
# Area planted with barley (x2): 0.0 hectares
# Maximum profit: 9999.999999999996
