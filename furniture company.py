# Note: This uses PuLP package which is a linear programming package
from pulp import *

# Furniture company problem: Maximize profit given constraints
prob = LpProblem("FurnitureCompany", LpMaximize)

# Variables: Number of chairs and tables to produce
chairs = LpVariable("Chairs", 0, None, LpInteger)
tables = LpVariable("Tables", 0, None, LpInteger)

# Objective function: Maximize profit
prob += 20 * chairs + 30 * tables, "Total Profit"

# Constraints
prob += 1 * chairs + 2 * tables <= 8, "Wood"
prob += 4 * chairs + 2 * tables <= 16, "Labor"
prob += 2 * chairs + 1 * tables <= 10, "Finishing"

# Solve
prob.solve()

print(f"Optimal production: Chairs = {value(chairs)}, Tables = {value(tables)}")
print(f"Maximum profit = ${value(prob.objective)}")