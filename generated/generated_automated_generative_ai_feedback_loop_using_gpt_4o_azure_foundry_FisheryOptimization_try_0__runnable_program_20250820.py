from ortools.linear_solver import pywraplp

def maximize_fish_transport():
    # Create the solver with the CBC backend
    solver = pywraplp.Solver.CreateSolver('CBC')
    if not solver:
        print("Solver not found!")
        return

    # Decision variables
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Objective function: Maximize total number of fish transported
    solver.Maximize(100 * x + 200 * y)

    # Constraints
    # 1. Cost constraint: 10 * x + 30 * y <= 100
    solver.Add(10 * x + 30 * y <= 100)

    # 2. Sled dog trips < truck trips (x < y)
    solver.Add(x + 1 <= y)

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f"OBJECTIVE={solver.Objective().Value()}")
        print(f"Number of sled dog trips: {x.solution_value()}")
        print(f"Number of truck trips: {y.solution_value()}")
    else:
        print("The problem does not have an optimal solution.")

# Run the program
maximize_fish_transport()
