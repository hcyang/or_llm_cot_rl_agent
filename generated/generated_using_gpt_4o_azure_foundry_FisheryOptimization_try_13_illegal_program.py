from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_d, f_t, c_d, c_t, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Truck trips

    # Define the constraints
    solver.Add(x < y)  # Sled dog trips must be less than truck trips
    solver.Add(c_d * x + c_t * y <= budget)  # Cost constraint

    # Define the objective function
    objective = solver.Maximize(f_d * x + f_t * y)

    # Solve the problem
    solver.Solve()

    # Get the results
    num_sled_dog_trips = x.solution_value()
    num_truck_trips = y.solution_value()
    max_fish_transport = solver.Objective().Value()

    return num_sled_dog_trips, num_truck_trips, max_fish_transport

# Example parameters
f_d = 100  # Fish per sled dog trip
f_t = 200  # Fish per truck trip
c_d = 30   # Cost per sled dog trip
c_t = 50   # Cost per truck trip
budget = 1000  # Maximum budget

# Get the solution
sled_dog_trips, truck_trips, max_fish = maximize_fish_transport(f_d, f_t, c_d, c_t, budget)

print(f"Sled Dog Trips: {sled_dog_trips}")
print(f"Truck Trips: {truck_trips}")
print(f"Maximum Fish Transported: {max_fish}")
