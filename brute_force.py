# brute force for activity selection (using time as constraint)

from itertools import combinations

def read_input_file(filename):
    activities = []
    with open(filename, 'r') as f:
        num_of_activities = int(f.readline().strip())  # reads first line (number of activities)

        constraints = f.readline().strip().split()  # reads second line (max time and budget)
        max_time = int(constraints[0])
        max_budget = int(constraints[1])

        # iterate through each following line in file
        for lines in range(num_of_activities):
            # split each line into a list of properties
            line = f.readline().strip().split()

            # assign properties to their respective variables
            name = line[0]
            time_required = int(line[1])
            cost = int(line[2])
            enjoyment = int(line[3])

            # store each activity as a dictionary
            activity = {
                'name': name,
                'time': time_required,
                'cost': cost,
                'enjoyment': enjoyment
            }
            activities.append(activity)

    return activities, max_time, max_budget


def brute_force(activities, max_time):
    total_activities = len(activities)  # count the total number of activities we have

    best_activities = []  # the best combination of activities
    max_enjoyment = 0  # the highest enjoyment value currently achieved

    # try all possible subset sizes (0 activities, 1 activity, etc)
    for subset_size in range(total_activities + 1):

        # for each subset size, generate all possible combinations of activities (as indicies)
        for subset_indices in combinations(range(total_activities), subset_size):

            # convert the indices into actual activities
            subset = []
            for i in subset_indices:
                subset.append(activities[i])

            # for the activities in the combination, add up the times
            total_time = 0
            for activity in subset:
                total_time += activity['time']

            """
            here would also be the place to check for the budget constraint.
            """

            # ensure it works with time constraint
            if total_time <= max_time:

                # for the activities in the combinatoin, add up the enjoyment
                total_enjoyment = 0
                for activity in subset:
                    total_enjoyment += activity['enjoyment']

                # if enjoyment is higher than the current best, replace the current best
                if total_enjoyment > max_enjoyment:
                    max_enjoyment = total_enjoyment
                    best_activities = subset

    # returns best combination and the enjoyment
    return best_activities, max_enjoyment


def print_solution(best_activities, max_enjoyment, max_time):
    print(f"Maximum Time Available: {max_time} hours")
    print(f"Optimal Enjoyment Value: {max_enjoyment}")
    print(f"Selected Activities: {len(best_activities)}")

    total_time = 0
    total_cost = 0

    for activity in best_activities:
        print(f"{activity['name']}:\nTime: {activity['time']}h Cost:{activity['cost']} Enjoyment: {activity['enjoyment']}\n")
        total_time += activity['time']
        total_cost += activity['cost']

    print(f"Total Time: {total_time} hours")
    print(f"Total Cost: {total_cost}")
    print(f"Total Enjoyment: {max_enjoyment}")


input_file = input('Enter name of input file: ')

# read input file
activities, max_time, max_budget = read_input_file(input_file)

# use brute force
best_activities, max_enjoyment = brute_force(activities, max_time)

# print the solution
print_solution(best_activities, max_enjoyment, max_time)

