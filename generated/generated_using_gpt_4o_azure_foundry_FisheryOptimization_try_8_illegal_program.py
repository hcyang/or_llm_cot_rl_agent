from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c_sled, c_truck, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None

    # Define decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # truck trips

    # Define the objective function
    objective = solver.Objective()
    objective.SetCoefficient(x, a)
    objective.SetCoefficient(y, b)
    objective.SetMaximization()

    # Define the constraints
    # Budget constraint
    solver.Add(c_sled * x + c_truck * y <= budget)
    
    # Sled dog trips less than truck trips
    solver.Add(x < y)

    # Solve the problem
    solver.Solve()

    # Get results
    num_sled_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish = objective.Value()

    return num_sled_trips, num_truck_trips, max_fish

# Example usage
a = 10  # Fish per sled dog trip
b = 20  # Fish per truck trip
c_sled = 5  # Cost per sled dog trip
c_truck = 8  # Cost per truck trip
budget = 100  # Total budget

result = maximize_fish_transport(a, b, c_sled, c_truck, budget)
print("Number of sled dog trips:", result[0])
print("Number of truck trips:", result[1])
print("Maximum number of fish transported:", result[2])
