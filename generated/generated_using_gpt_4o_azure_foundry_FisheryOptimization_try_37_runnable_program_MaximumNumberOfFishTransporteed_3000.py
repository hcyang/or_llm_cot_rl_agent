from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_trip_dogs, fish_per_trip_trucks, 
                            cost_per_trip_dogs, cost_per_trip_trucks, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables
    x = solver.NumVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.NumVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function
    solver.Maximize(fish_per_trip_dogs * x + fish_per_trip_trucks * y)

    # Add the constraints
    solver.Add(cost_per_trip_dogs * x + cost_per_trip_trucks * y <= budget)
    solver.Add(x <= y - 1)  # x < y

    # Solve the problem
    status = solver.Solve()

    # Check the solution status
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips =', x.solution_value())
        print('Number of truck trips =', y.solution_value())
        print('Maximum number of fish transported =', solver.Objective().Value())
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example parameters
fish_per_trip_dogs = 100  # Number of fish per sled dog trip
fish_per_trip_trucks = 300  # Number of fish per truck trip
cost_per_trip_dogs = 50  # Cost per sled dog trip
cost_per_trip_trucks = 100  # Cost per truck trip
budget = 1000  # Total budget available

# Run the function
maximize_fish_transport(fish_per_trip_dogs, fish_per_trip_trucks, 
                        cost_per_trip_dogs, cost_per_trip_trucks, budget)
