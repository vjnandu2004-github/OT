import math

def eoq(demand, order_cost, holding_cost):
    """
    Calculate Economic Order Quantity
    demand = annual demand
    order_cost = cost per order
    holding_cost = annual holding cost per unit
    """
    eoq = math.sqrt((2 * demand * order_cost) / holding_cost)
    num_orders = demand / eoq
    cycle_time = 365 / num_orders
    total_cost = (demand / eoq) * order_cost + (eoq / 2) * holding_cost
    
    return {
        'EOQ': eoq,
        'Number of Orders per Year': num_orders,
        'Cycle Time (days)': cycle_time,
        'Total Annual Cost': total_cost
    }

# Example usage
result = eoq(10000, 150, 2.5)
for key, value in result.items():
    print(f"{key}: {value:.2f}")