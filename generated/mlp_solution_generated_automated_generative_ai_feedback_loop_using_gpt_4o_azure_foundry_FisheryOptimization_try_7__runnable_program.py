from ortools.linear_solver import pywraplp

def main():
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Variables
    # x: number of sled dog trips
    # y: number of truck trips
    x = solver.IntVar(0, solver.infinity(), 'x')
    y = solver.IntVar(0, solver.infinity(), 'y')

    # Constraints
    # Cost constraint: 10 * x + 30 * y <= 100
    solver.Add(10 * x + 30 * y <= 100)

    # x < y is equivalent to x <= y - 1
    solver.Add(x <= y - 1)

    # Objective: Maximize the number of fish transported
    # Objective function: 100 * x + 200 * y
    solver.Maximize(100 * x + 200 * y)

    # Solve the problem
    status = solver.Solve()

    # Check the solution
    if status == pywraplp.Solver.OPTIMAL:
        print(f'OBJECTIVE= {solver.Objective().Value()}')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()
