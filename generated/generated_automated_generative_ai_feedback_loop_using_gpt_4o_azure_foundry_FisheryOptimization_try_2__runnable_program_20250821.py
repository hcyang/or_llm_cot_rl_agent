from ortools.linear_solver import pywraplp

def main():
    # Create the MIP solver with SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        print("SCIP solver not found.")
        return

    # Variables
    # Let x = number of sled dog trips (integer variable).
    # Let y = number of truck trips (integer variable).
    x = solver.IntVar(0, solver.infinity(), 'x')  # Number of sled dog trips
    y = solver.IntVar(0, solver.infinity(), 'y')  # Number of truck trips

    # Constraints
    # 1. Cost constraint: 10 * x + 30 * y <= 100
    solver.Add(10 * x + 30 * y <= 100)

    # 2. Number of sled dog trips must be less than the number of truck trips: x < y
    # Since OR-Tools does not support strict inequalities, we rewrite it as: x <= y - 1
    solver.Add(x <= y - 1)

    # Objective: Maximize the number of fish transported
    # Objective function: 100 * x + 200 * y
    objective = solver.Objective()
    objective.SetCoefficient(x, 100)  # 100 fish per sled dog trip
    objective.SetCoefficient(y, 200)  # 200 fish per truck trip
    objective.SetMaximization()

    # Solve the problem
    status = solver.Solve()

    # Check the result
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Number of sled dog trips (x): {x.solution_value()}")
        print(f"Number of truck trips (y): {y.solution_value()}")
        print(f"OBJECTIVE={objective.Value()}")
    else:
        print("The solver could not find an optimal solution.")

if __name__ == '__main__':
    main()
