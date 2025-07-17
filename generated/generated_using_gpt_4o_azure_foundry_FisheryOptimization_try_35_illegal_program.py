from ortools.linear_solver import pywraplp

def maximize_fish_transport(F_s, F_t, C_s, C_t, B):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Truck trips

    # Define the constraints
    # Constraint 1: Total cost constraint
    solver.Add(C_s * x + C_t * y <= B)

    # Constraint 2: Sled dog trips must be less than truck trips
    solver.Add(x < y)

    # Define the objective function: Maximize number of fish transported
    objective = solver.Objective()
    objective.SetCoefficient(x, F_s)
    objective.SetCoefficient(y, F_t)
    objective.SetMaximization()

    # Solve the problem
    solver.Solve()

    # Retrieve the solution
    num_sled_dog_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish_transported = objective.Value()

    return num_sled_dog_trips, num_truck_trips, max_fish_transported

# Example usage
F_s = 100  # Number of fish per sled dog trip
F_t = 200  # Number of fish per truck trip
C_s = 50   # Cost per sled dog trip
C_t = 100  # Cost per truck trip
B = 5000   # Total budget

sled_dog_trips, truck_trips, max_fish = maximize_fish_transport(F_s, F_t, C_s, C_t, B)
print(f"Sled dog trips: {sled_dog_trips}")
print(f"Truck trips: {truck_trips}")
print(f"Maximum fish transported: {max_fish}")
