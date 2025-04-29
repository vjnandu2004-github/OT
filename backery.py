from pulp import *

prob = LpProblem("BakeryProblem", LpMaximize)

# Variables: Number of cakes and breads to produce
cakes = LpVariable("Cakes", 0, None, LpInteger)
breads = LpVariable("Breads", 0, None, LpInteger)

# Objective function: Maximize profit
prob += 15 * cakes + 10 * breads, "Total Profit"

# Constraints
prob += 2 * cakes + 1 * breads <= 20, "Flour"
prob += 1 * cakes + 1 * breads <= 15, "Sugar"
prob += 3 * cakes + 2 * breads <= 30, "Eggs"

# Solve
prob.solve()

print(f"Optimal production: Cakes = {value(cakes)}, Breads = {value(breads)}")
print(f"Maximum profit = ${value(prob.objective)}")