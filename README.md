# Student Society Event Planner - README

## Overview

This project was developed for the ECM1414 Algorithms and Data Structures coursework.
It is an **Event Planner** that selects the best combination of activities to maximise enjoyment.
It does this while considering various constraints.

The program compares:

* A brute-force algorithm *(exhaustive search)*
* A dynamic programming algorithm *(more efficient approach)*

Both algorithms process the same input and output the chosen activities, totals, and execution time.

---

## Files Included

* **event_planner_with_extension.py** - Includes brute force and dynamic programming implementation with extension
* **event_planner.py** - Includes brute force and dynamic programming implementation without extension
* **brute_force.py** - Standalone brute-force implementation
* **brute_force_extension.py** - Version checking both time and budget
* **pseudocode brute force.txt** - Brute-force algorithm pseudocode
* **final code pseudocode.txt** - Pseudocode for event_planner.py
* **README.md** - This file

---

## Requirements

* Python 3 + standard included libraries

---

## Running the Program

### Main version

```bash
python event_planner_with_extension.py
```
or, for the version without the extension:
```bash
python event_planner.py
```

Note: the directory structure must be as follows
```
project/
    code/
        event_planner_with_extension.py
        event_planner.py
    Input_Files/
      input_small.txt
      input_medium.txt
      input_large.txt
```
### Brute-force only version

```bash
python "brute_force_with_extension.py"
```
or, for the version without the extension:
```bash
python "brute_force.py"
```

Enter the input filename when asked (must be in the same directory as Brute Force.py).

---

## Input File Format

Text file structure:

```
n
T B
ActivityName Time Cost Enjoyment
...
```

* n = number of activities
* T = max time
* B = max budget

---
## Output

For each algorithm the program displays:
  1. Input File, which shows the name of the input file being used
  2. Selected Activities: List of chosen activities with time, cost, and enjoyment
  3. Total Enjoyment: Sum of enjoyment values
  4. Total Time Used: Sum of time required
  5. Total Cost: Sum of costs
  6. Available Time and Budget, which displays constraints
  7. Execution Time: Time taken by the algorithm

Below is an example output of what you can expect when running the code using `input_small.txt`. Execution times may vary.
```bash
========================================
EVENT PLANNER - RESULTS
========================================
Input File: input_small.txt
Available Time: 10 hours
Available Budget: £200
--- BRUTE FORCE ALGORITHM ---
Selected Activities:
- Game-Night (3 hours, £80, enjoyment 120)
- Pizza-Workshop (2 hours, £60, enjoyment 100)
- Hiking (5 hours, £30, enjoyment 140)
Total Enjoyment: 360
Total Time Used: 10 hours
Total Cost: £170
Execution Time: 0.002 seconds
--- DYNAMIC PROGRAMMING ALGORITHM ---
Selected Activities:
- Game-Night (3 hours, £80, enjoyment 120)
- Pizza-Workshop (2 hours, £60, enjoyment 100)
- Hiking (5 hours, £30, enjoyment 140)
Total Enjoyment: 360
Total Time Used: 10 hours
Total Cost: £170
Execution Time: 0.001 seconds
========================================

```

---

## Notes

* Each activity can be selected only once.
* Time is treated as the primary constraint in the core implementation.
* Both time and budget constraints are respected in exetension implementation
* Both algorithms are run on the same input for performance comparison


