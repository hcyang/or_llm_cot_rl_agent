from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Define constraints
    # Budget constraint
    solver.Add(c * x + d * y <= B)
    
    # Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Objective function: Maximize the number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(x, a)
    objective.SetCoefficient(y, b)
    objective.SetMaximization()

    # Solve the problem
    solver.Solve()

    # Get the results
    x_value = x.solution_value()
    y_value = y.solution_value()
    objective_value = objective.Value()

    return x_value, y_value, objective_value

# Example parameters
a = 100  # Fish per sled dog trip
b = 300  # Fish per truck trip
c = 50   # Cost per sled dog trip
d = 120  # Cost per truck trip
B = 1000 # Budget

x_value, y_value, objective_value = maximize_fish_transport(a, b, c, d, B)
print(f"Number of sled dog trips: {x_value}")
print(f"Number of truck trips: {y_value}")
print(f"Maximum number of fish transported: {objective_value}")
