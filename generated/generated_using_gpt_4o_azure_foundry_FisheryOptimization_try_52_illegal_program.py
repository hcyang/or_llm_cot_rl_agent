from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled_dog_trip, fish_per_truck_trip, cost_per_sled_dog_trip, cost_per_truck_trip, budget_limit):
    # Create the solver.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Define the decision variables.
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Define the objective function.
    solver.Maximize(fish_per_sled_dog_trip * x + fish_per_truck_trip * y)

    # Define the constraints.
    solver.Add(cost_per_sled_dog_trip * x + cost_per_truck_trip * y <= budget_limit)
    solver.Add(x < y)

    # Solve the problem.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Number of sled dog trips:', x.solution_value())
        print('Number of truck trips:', y.solution_value())
        print('Maximum number of fish transported:', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

# Example usage
maximize_fish_transport(
    fish_per_sled_dog_trip=100,  # Example value for fish per sled dog trip
    fish_per_truck_trip=200,     # Example value for fish per truck trip
    cost_per_sled_dog_trip=50,   # Example value for cost per sled dog trip
    cost_per_truck_trip=150,     # Example value for cost per truck trip
    budget_limit=1000            # Example budget limit
)
