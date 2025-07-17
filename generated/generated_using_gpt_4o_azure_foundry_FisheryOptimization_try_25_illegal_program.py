from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips
    
    # Define the objective function
    solver.Maximize(a * x + b * y)
    
    # Define the constraints
    solver.Add(c * x + d * y <= budget)  # Cost constraint
    solver.Add(x < y)  # Sled dog trips less than truck trips
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value (max fish): {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        return solver.Objective().Value()
    else:
        print('No optimal solution found.')
        return None

# Example usage
a = 100  # Fish per sled dog trip
b = 200  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 150  # Cost per truck trip
budget = 1000  # Total budget

maximize_fish_transport(a, b, c, d, budget)
