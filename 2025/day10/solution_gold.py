import re
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

data = []
# Create an array where target is an array of the button presses
# and the buttons are an array of length target,
# buttons are 1s and 0s, where 1 shows a button in that position
with open("input.txt", "r") as f:
    for line in f:
        target = [int(n) for n in re.findall(
            r'\{([^\]]*)\}', line)[0].split(",")]
        parens = re.findall(r'\(([^)]*)\)', line)
        buttons = []
        for combo in parens:
            indices = [int(n) for n in combo.split(",")]
            buttonPositions = [
                1 if i in indices else 0 for i in range(len(target))]
            buttons.append(buttonPositions)

        data.append((target, buttons))

# References for Integer Linear Programming
# https://www.youtube.com/watch?v=E72DWgKP_1Y&t=841s
# https://en.wikipedia.org/wiki/Integer_programming
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html


def minPressses(target, buttons):
    """
    Example: target = [3, 5], buttons = [[1,0], [0,1], [1,1]]

    This means:
    - Counter 0 must reach 3, Counter 1 must reach 5
    - Button 0 (presses=b0) adds 1 to counter 0 only
    - Button 1 (presses=b1) adds 1 to counter 1 only
    - Button 2 (presses=b2) adds 1 to both counters

    We need to solve:
        1*b0 + 0*b1 + 1*b2 = 3   (counter 0 equation)
        0*b0 + 1*b1 + 1*b2 = 5   (counter 1 equation)

    While minimizing: b0 + b1 + b2 (total presses)
    """
    numButtons = len(buttons)

    # A = coefficient matrix for the equations
    # Rows = counters, Columns = buttons
    # A[i][j] = "does button j affect counter i?" (1 or 0)
    #
    # Example with buttons = [[1,0], [0,1], [1,1]]:
    #   buttons as stored:  [[1,0], [0,1], [1,1]]  (each row is a button)
    #   after .T transpose: [[1,0,1], [0,1,1]]     (each row is a counter)
    #
    # So A = [[1, 0, 1],   ← counter 0: affected by buttons 0 and 2
    #         [0, 1, 1]]   ← counter 1: affected by buttons 1 and 2
    A = np.array(buttons).T

    # B = target values for each counter
    # Example: B = [3, 5] means counter 0 must equal 3, counter 1 must equal 5
    B = np.array(target)

    # c = coefficients for the goal function (what we minimize)
    # The solver minimizes: c[0]*b0 + c[1]*b1 + c[2]*b2 + ...
    # With all 1s, this is just: 1*b0 + 1*b1 + 1*b2 = total presses
    # i.e. each button press is equally weighted
    c = np.ones(numButtons)

    result = milp(
        # GOAL: minimize c[0]*b0 + c[1]*b1 + ... (total presses)
        c=c,

        # CONSTRAINTS: A × [b0, b1, b2, ...] must equal B
        # LinearConstraint(A, lower_bound, upper_bound)
        # Setting both bounds to B means: A × presses == B (exact equality)
        constraints=LinearConstraint(A, B, B),  # type: ignore

        # BOUNDS: each variable (button presses) must be >= 0
        # Can't press a button negative times
        bounds=Bounds(lb=0),

        # INTEGRALITY: all variables must be integers
        # Can't press a button 2.5 times
        # (array of 1s means "yes, this variable is an integer")
        integrality=c
    )

    # result.fun = the minimum value of our goal (total presses)
    # result.x = the actual values [b0, b1, b2, ...] that achieve this
    return int(round(result.fun))


solution = 0
for target, buttons in data:
    solution += minPressses(target, buttons)

print(solution)
