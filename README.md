# Student Society Event Planner - README

## Overview

This project was developed for the ECM1414 Algorithms and Data Structures coursework.
It is an **Event Planner** that selects the best combination of activities to maximise enjoyment while respecting constraints (primarily available time).

The program compares:

* A brute-force algorithm *(exhaustive search)*
* A dynamic programming algorithm *(more efficient approach)*

Both algorithms process the same input and output the chosen activities, totals, and execution time.

---

## Files

* **Final_code_without_extension.py** - Includes dynamic programming implementation
* **Brute Force.py** - Standalone brute-force implementation
* **Brute Force Extension.py** - Version checking both time and budget
* **constraints_4_2.py** - Constraint helper functions
* **pseudocode brute force.txt** - Brute force algorithm pseudocode
* **README.md** - This file

---

## Requirements

* Python 3 + standard included libraries

---

## Running the Program

### Main version

```bash
python Final_code_without_extension.py
```

Note: the directory structure must be as follows

project/
    code/
        Final_code_without_extension.py
    Input_Files/
      input_small.txt
      input_medium.txt
      input_large.txt

### Brute-force only version

```bash
python "Brute Force.py"
```

Enter the input filename when asked (must be in the same directory as Brute Force.py).

---

## Input Format

Text file structure:

```
n
T B
ActivityName Time Cost Enjoyment
...
```

* `n` = number of activities
* `T` = max time
* `B` = max budget

---

## Notes

* Each activity can be selected only once.
* Time is treated as the primary constraint in the core implementation.


