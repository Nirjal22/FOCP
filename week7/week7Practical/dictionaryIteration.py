# TASK: Write some code that iterates over the contents of the roots dictionary created
# within an earlier task. For each entry, print the message -
# “The square root of <num> is <sqrt>”
# Where <num> shows the number, and <sqrt> shows the square root of that number.

import math


roots = {n: math.sqrt(n) for n in range(1, 26)}

for num, sqrt_value in roots.items():
    print(f"The square root of {num} is {sqrt_value}")
