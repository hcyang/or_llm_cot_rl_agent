from ortools.linear_solver import pywraplp

def maximize_fish_transport(a, b, c, d, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    if not solver:
        return "Solver not found."

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Define the objective function
    solver.Maximize(a * x + b * y)

    # Define the constraints
    solver.Add(c * x + d * y <= B)    # Budget constraint
    solver.Add(x < y)                 # Sled trips less than truck trips

    # Solve the problem
    solver.Solve()

    # Get the results
    num_sled_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish_transported = a * num_sled_trips + b * num_truck_trips

    return {
        "num_sled_trips": num_sled_trips,
        "num_truck_trips": num_truck_trips,
        "max_fish_transported": max_fish_transported
    }

# Example parameters
a = 100   # Fish per sled dog trip
b = 300   # Fish per truck trip
c = 50    # Cost per sled dog trip
d = 150   # Cost per truck trip
B = 1000  # Total budget

solution = maximize_fish_transport(a, b, c, d, B)
print(solution)
