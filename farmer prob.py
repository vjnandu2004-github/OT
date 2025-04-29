# Again using PuLP for demonstration
from pulp import *

prob = LpProblem("FarmerProblem", LpMaximize)

# Variables: Acres of wheat and barley to plant
wheat = LpVariable("Wheat", 0, None)
barley = LpVariable("Barley", 0, None)

# Objective function: Maximize profit
prob += 120 * wheat + 80 * barley, "Total Profit"

# Constraints
prob += wheat + barley <= 100, "Land"
prob += 2 * wheat + barley <= 150, "Labor"
prob += wheat >= 40, "Wheat demand"
prob += barley >= 30, "Barley demand"

# Solve
prob.solve()

print(f"Optimal planting: Wheat = {value(wheat)} acres, Barley = {value(barley)} acres")
print(f"Maximum profit = ${value(prob.objective)}")