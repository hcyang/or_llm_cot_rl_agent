from ortools.linear_solver import pywraplp

def maximize_fish_transport(f_s, f_t, c_s, c_t, B):
    # Create the linear solver with the GLOP backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the constraints
    solver.Add(c_s * x + c_t * y <= B)  # Budget constraint
    solver.Add(x < y)  # Sled dog trips must be less than truck trips

    # Define the objective function
    solver.Maximize(f_s * x + f_t * y)

    # Solve the problem
    solver.Solve()

    # Return the solution
    return {
        'objective_value': solver.Objective().Value(),
        'sled_dog_trips': x.solution_value(),
        'truck_trips': y.solution_value()
    }

# Example usage
f_s = 100  # Number of fish per sled dog trip
f_t = 500  # Number of fish per truck trip
c_s = 10   # Cost per sled dog trip
c_t = 50   # Cost per truck trip
B = 1000   # Total budget

solution = maximize_fish_transport(f_s, f_t, c_s, c_t, B)
print('Maximized number of fish:', solution['objective_value'])
print('Number of sled dog trips:', solution['sled_dog_trips'])
print('Number of truck trips:', solution['truck_trips'])
