import os
import sys
import itertools
import time


# 1. Input handling
def read_input_file(filename):
    activities = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        max_time, max_budget = map(int, f.readline().strip().split())
        for i in range(n):
            line = f.readline().strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 4:
                print(f"Skipping invalid line: {line}")
                continue
            name = parts[0]
            time_required = int(parts[1])
            cost = int(parts[2])
            enjoyment = int(parts[3])
            activities.append({
                'name': name,
                'time': time_required,
                'cost': cost,
                'enjoyment': enjoyment
            })
    return activities, max_time, max_budget


# 2. Brute-force algorithm (both constraints)
def brute_force(activities, max_time, max_budget):
    max_enjoyment = 0
    best_activities = []
    for s in range(len(activities) + 1):
        for subset in itertools.combinations(activities, s):
            total_time = sum(activity['time'] for activity in subset)
            total_cost = sum(activity['cost'] for activity in subset)
            # Check BOTH time and budget constraints
            if total_time <= max_time and total_cost <= max_budget:
                total_enjoyment = sum(activity['enjoyment'] for activity in subset)
                if total_enjoyment > max_enjoyment:
                    max_enjoyment = total_enjoyment
                    best_activities = subset
    return best_activities, max_enjoyment


# 3. Dynamic programming algorithm (both constraints)
def dynamic_programming(activities, max_time, max_budget):
    n = len(activities)
    # 3D table: [activity][time][budget]
    dp = []
    for i in range(n + 1):
        time_layer = []
        for t in range(max_time + 1):
            time_layer.append([0] * (max_budget + 1))
        dp.append(time_layer)

    for i in range(1, n + 1):
        activity = activities[i - 1]
        for t in range(max_time + 1):
            for c in range(max_budget + 1):
                # Check if activity fits within both remaining time and budget
                if activity['time'] <= t and activity['cost'] <= c:
                    skip = dp[i - 1][t][c]
                    include = dp[i - 1][t - activity['time']][c - activity['cost']] + activity['enjoyment']
                    dp[i][t][c] = max(skip, include)
                else:
                    dp[i][t][c] = dp[i - 1][t][c]

    # Backtrack to find selected activities
    t = max_time
    c = max_budget
    best_activities = []
    for i in range(n, 0, -1):
        if dp[i][t][c] != dp[i - 1][t][c]:
            activity = activities[i - 1]
            best_activities.append(activity)
            t -= activity['time']
            c -= activity['cost']
    best_activities.reverse()
    max_enjoyment = dp[n][max_time][max_budget]
    return best_activities, max_enjoyment


# 4. Greedy heuristic  - Extension 3
def greedy_heuristic(activities, max_time, max_budget):
    """
    EXTENSION 3: Greedy heuristic.
    Scores each activity by enjoyment per hour, selects highest ratio first,
    only adding activities that fit within BOTH remaining time and budget.
    """
    if not activities:
        return [], 0

    # Score by enjoyment per hour
    scored = []
    for activity in activities:
        ratio = activity['enjoyment'] / activity['time'] if activity['time'] > 0 else 0
        scored.append((ratio, activity))

    # Sort highest ratio first
    scored.sort(key=lambda x: x[0], reverse=True)

    selected = []
    time_left = max_time
    budget_left = max_budget

    for _, activity in scored:
        # Check BOTH time and budget constraints
        if activity['time'] <= time_left and activity['cost'] <= budget_left:
            selected.append(activity)
            time_left -= activity['time']
            budget_left -= activity['cost']

    total_enjoyment = sum(a['enjoyment'] for a in selected)
    return selected, total_enjoyment


# 5. Print results
def results(label, best_activities, max_enjoyment, exec_time):
    print(f"--- {label} ---")
    if best_activities:
        print("Selected Activities:")
        for a in best_activities:
            print(f"- {a['name']} ({a['time']} hours, £{a['cost']}, enjoyment {a['enjoyment']})")
    else:
        print("No activities were selected.")

    total_time_used = sum(a['time'] for a in best_activities)
    total_cost_used = sum(a['cost'] for a in best_activities)

    print(f"Total Enjoyment: {max_enjoyment}")
    print(f"Total Time Used: {total_time_used} hours")
    print(f"Total Cost: £{total_cost_used}")
    print(f"Execution Time: {exec_time:.6f} seconds\n")


# 6. Main execution
def event_planner_summary():
    while True:
        size = input("Please, enter the input size (small, medium, large) or in order to exit press 'e': ").lower()
        if size == 'e':
            break
        if size not in ('small', 'medium', 'large'):
            print("Incorrect input, please choose: small, medium, or large.")
            continue

        filename = os.path.join(os.path.dirname(__file__), '..', 'Input_Files', f'input_{size}.txt')
        if not os.path.exists(filename):
            print(f"Input file not found: {filename}")
            continue

        activities, max_time, max_budget = read_input_file(filename)

        print("========================================")
        print("EVENT PLANNER - RESULTS")
        print("========================================")
        print(f"Input File: {os.path.basename(filename)}")
        print(f"Available Time: {max_time} hours")
        print(f"Available Budget: £{max_budget}\n")

        # Brute-force
        start = time.time()
        best_activities, max_enjoyment = brute_force(activities, max_time, max_budget)
        bf_time = time.time() - start
        results("BRUTE FORCE ALGORITHM", best_activities, max_enjoyment, bf_time)

        # Dynamic Programming
        start = time.time()
        best_activities, max_enjoyment = dynamic_programming(activities, max_time, max_budget)
        dp_time = time.time() - start
        results("DYNAMIC PROGRAMMING ALGORITHM", best_activities, max_enjoyment, dp_time)

        # Greedy Heuristic (Extension 3)
        start = time.time()
        greedy_activities, greedy_enjoyment = greedy_heuristic(activities, max_time, max_budget)
        greedy_time = time.time() - start
        results("GREEDY HEURISTIC (Extension 3)", greedy_activities, greedy_enjoyment, greedy_time)

        # Comparison summary
        print("========================================")
        print("ALGORITHM COMPARISON SUMMARY")
        print("========================================")
        print(f"Brute Force:         {max_enjoyment} enjoyment  ({bf_time:.6f}s)")
        print(f"Dynamic Programming: {max_enjoyment} enjoyment  ({dp_time:.6f}s)")
        if max_enjoyment > 0:
            pct = (greedy_enjoyment / max_enjoyment) * 100
            print(f"Greedy Heuristic:    {greedy_enjoyment} enjoyment  ({greedy_time:.6f}s) — {pct:.1f}% of optimal")
        else:
            print(f"Greedy Heuristic:    {greedy_enjoyment} enjoyment  ({greedy_time:.6f}s)")
        print("========================================\n")


if __name__ == "__main__":
    event_planner_summary()
