# constraints.py
# Shared constraint logic for activity selection

def satisfies_constraints(selection, max_time, max_budget):
    

    total_time = 0
    total_cost = 0

    for activity in selection:
        total_time += activity['time']
        total_cost += activity['cost']

    return total_time <= max_time and total_cost <= max_budget
