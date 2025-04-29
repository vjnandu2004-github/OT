import math
import matplotlib.pyplot as plt
import numpy as np

class InventoryManager:
    def __init__(self, annual_demand, order_cost, holding_cost_per_unit, lead_time_days):
        self.annual_demand = annual_demand
        self.order_cost = order_cost
        self.holding_cost = holding_cost_per_unit
        self.lead_time = lead_time_days
        self.eoq_data = self.calculate_eoq()
        
    def calculate_eoq(self):
        eoq = math.sqrt((2 * self.annual_demand * self.order_cost) / self.holding_cost)
        orders_per_year = self.annual_demand / eoq
        cycle_time = 365 / orders_per_year
        reorder_point = (self.annual_demand / 365) * self.lead_time
        total_cost = (self.annual_demand / eoq) * self.order_cost + (eoq / 2) * self.holding_cost
        
        return {
            'EOQ': eoq,
            'Orders per Year': orders_per_year,
            'Cycle Time (days)': cycle_time,
            'Reorder Point': reorder_point,
            'Total Cost': total_cost
        }
    
    def plot_inventory_levels(self, periods=3):
        eoq = self.eoq_data['EOQ']
        cycle_time = self.eoq_data['Cycle Time (days)']
        lead_time = self.lead_time
        
        # Create time points
        time_points = np.linspace(0, periods * cycle_time, 1000)
        inventory_levels = []
        
        for t in time_points:
            cycle_num = t // cycle_time
            time_in_cycle = t % cycle_time
            if time_in_cycle < (cycle_time - lead_time):
                inventory = eoq - (eoq / (cycle_time - lead_time)) * time_in_cycle
            else:
                inventory = 0
            inventory_levels.append(inventory)
        
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, inventory_levels, label='Inventory Level')
        plt.axhline(y=self.eoq_data['Reorder Point'], color='r', linestyle='--', label='Reorder Point')
        
        for i in range(periods + 1):
            plt.axvline(x=i * cycle_time, color='g', linestyle=':', alpha=0.5)
        
        plt.title('Inventory Level Over Time')
        plt.xlabel('Time (days)')
        plt.ylabel('Inventory Level')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def sensitivity_analysis(self, demand_range=(0.5, 1.5), steps=10):
        """Analyze how EOQ changes with demand"""
        demand_factors = np.linspace(demand_range[0], demand_range[1], steps)
        demands = self.annual_demand * demand_factors
        eoqs = []
        costs = []
        
        for d in demands:
            eoq = math.sqrt((2 * d * self.order_cost) / self.holding_cost)
            total_cost = (d / eoq) * self.order_cost + (eoq / 2) * self.holding_cost
            eoqs.append(eoq)
            costs.append(total_cost)
        
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.plot(demands, eoqs, 'b-o')
        plt.title('EOQ vs Demand')
        plt.xlabel('Annual Demand')
        plt.ylabel('EOQ')
        plt.grid(True)
        
        plt.subplot(1, 2, 2)
        plt.plot(demands, costs, 'r-o')
        plt.title('Total Cost vs Demand')
        plt.xlabel('Annual Demand')
        plt.ylabel('Total Annual Cost')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()

# Example usage
company = InventoryManager(
    annual_demand=10000,
    order_cost=150,
    holding_cost_per_unit=2.5,
    lead_time_days=5
)

# Print EOQ results
print("EOQ Analysis Results:")
for key, value in company.eoq_data.items():
    print(f"{key}: {value:.2f}")

# Plot inventory levels
company.plot_inventory_levels()

# Perform sensitivity analysis
company.sensitivity_analysis()