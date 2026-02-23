import os
import sys
import itertools
import time


# 1. Handiling of an input
def read_input_file(filename):
    activities = []
    with open(filename, 'r') as f:
        # Checks how many activities we have by reading the given file.
        n = int(f.readline().strip())
        # By using map we do a shortcut to do it one time, by coverting several strings to integers.
        max_time, max_budget = map(int, f.readline().strip().split())
        # Reads lines and skips if line is empty.
        for i in range(n):
            line = f.readline().strip()
            if not line:
                continue
            # By splitting line into parts we can skip the lines that can lead code to failure.
            parts = line.split()
            # Number four refers to 4 parts: name, time, cost and enjoyment.
            if len(parts) < 4:
                print(f"Skipping invalid line: {line}")
                continue
            name = parts[0]
            time_required = int(parts[1])
            cost = int(parts[2])
            enjoyment = int(parts[3])
            # For more convinient use, we store activity as dictionary.
            activities.append({
                'name': name,
                'time': time_required,
                'cost': cost,
                'enjoyment': enjoyment
            })
    return activities, max_time, max_budget


# 2. Brute-force algorithm
def brute_force(activities, max_time):
    # We try to find the best combination of given activities.
    max_enjoyment = 0
    best_activities = []
    # Check every possible number of our given activities.
    for s in range(len(activities) + 1):
        # By using Python Library itertools, we generate all possible combinations of length of s,
        # which is as stated above from 0 up to len(activities).
        for subset in itertools.combinations(activities, s):
            # Check that we only consider subsets that are suitable for available time.
            total_time = sum(activity['time'] for activity in subset)
            if total_time <= max_time:
                # Calculate the total enjoyment of the current subset.
                total_enjoyment = sum(activity['enjoyment'] for activity in subset)
                if total_enjoyment > max_enjoyment:
                    # Update previously stated max_enjoyment and best_activities.
                    max_enjoyment = total_enjoyment
                    best_activities = subset
    return best_activities, max_enjoyment


# 3. Dynamic programming algorithm
def dynamic_programming(activities, max_time):
    n = len(activities)
    # Create the table in 2D in which we will store achievable maximum enjoyment.
    max_enjoyment_table = []
    for j in range(n+1):
        max_enjoyment_table .append([0]*(max_time+1))

    for i in range(1, n+1):
        activity = activities[i-1]
        for t in range(max_time+1):
            # Check if our activity is suitable for left time.
            # Check what happends if it fits.
            if activity['time'] <= t:
                # We have then two choices: skip the activity or include it.
                # Skip the current activity.
                skip_activity = max_enjoyment_table[i-1][t]

                # Include the current activity.
                include_activity = max_enjoyment_table[i-1][t - activity['time']] + activity['enjoyment']

                # Choose the option with higher total enjoyment.
                max_enjoyment_table[i][t] = max(skip_activity, include_activity)
            else:
                # Include the possibility when activity does not fit.
                max_enjoyment_table[i][t] = max_enjoyment_table[i-1][t]

    # Check which activities were chosen for the maximum enjoyment.
    t = max_time
    best_activities = []
    # We loop from end to beginning to see which activities contributes to the maximum enjoyment.

    for i in range(n, 0, -1):
        # Check if this activity was included in possible solution.
        if max_enjoyment_table [i][t] != max_enjoyment_table [i-1][t]:
            # Get the activity which has maximum enjoyment.
            activity = activities[i-1]
            best_activities.append(activity)
            # Reduce remaining time by this activity's time.
            t -= activity['time']
    # Fix the order as we iterated from the end.
    best_activities.reverse()
    max_enjoyment = max_enjoyment_table [n][max_time]
    return best_activities, max_enjoyment



# 4. Print of the results
def results(label, best_activities, max_enjoyment, exec_time):
    print(f"--- {label} ---")
    # Check if any activities where selected.
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


# 5. Main execution
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
            print(f"Input file is not found: {filename}")
            continue

        # Read the activities.
        activities, max_time, max_budget = read_input_file(filename)

        print("========================================")
        print("EVENT PLANNER - RESULTS")
        print("========================================")
        print(f"Input File: {os.path.basename(filename)}")
        print(f"Available Time: {max_time} hours")
        print(f"Available Budget: £{max_budget}\n")


        # Brute-force
        start = time.time()
        best_activities, max_enjoyment = brute_force(activities, max_time)
        # Calculate how much time did the brute-force algorithm take.
        bf_time = time.time() - start
        results("BRUTE FORCE ALGORITHM", best_activities, max_enjoyment, bf_time)

        # Dynamic Programming
        start = time.time()
        best_activities, max_enjoyment = dynamic_programming(activities, max_time)
        # Calculate how much time did the dynamic-programming algorithm take.
        dp_time = time.time() - start
        results("DYNAMIC PROGRAMMING ALGORITHM", best_activities, max_enjoyment, dp_time)

        # PLS CHECK IF WE NEED TO INCLUDE NOTES HERE: Algorithm Complexity THROUGH PRINT

if __name__ == "__main__":
    event_planner_summary()



if __name__ == "__main__":
    event_planner_summary()
