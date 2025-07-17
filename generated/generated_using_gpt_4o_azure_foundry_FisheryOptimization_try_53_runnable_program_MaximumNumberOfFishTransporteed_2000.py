from ortools.linear_solver import pywraplp

def maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    if not solver:
        return None
    
    # Decision variables: number of sled dog trips (x) and truck trips (y)
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    
    # Objective function: Maximize fish transported
    solver.Maximize(fish_per_sled * x + fish_per_truck * y)
    
    # Constraints
    # Budget constraint
    solver.Add(cost_per_sled * x + cost_per_truck * y <= budget)
    
    # Sled dog trips must be less than truck trips
    solver.Add(x <= y - 1)
    
    # Solve the problem
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution found:')
        print(f'Number of sled dog trips: {x.solution_value()}')
        print(f'Number of truck trips: {y.solution_value()}')
        print(f'Maximum number of fish transported: {solver.Objective().Value()}')
        return solver.Objective().Value()
    else:
        print('The problem does not have an optimal solution.')
        return None

# Example usage
fish_per_sled = 100  # number of fish per sled dog trip
fish_per_truck = 200  # number of fish per truck trip
cost_per_sled = 50    # cost per sled dog trip
cost_per_truck = 100  # cost per truck trip
budget = 1000         # total budget

maximize_fish_transport(fish_per_sled, fish_per_truck, cost_per_sled, cost_per_truck, budget)
