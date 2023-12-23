"""Use an editor to input another Python program utils_test.py. This program
should import my_utils then call the average() function several times, passing a list of
values as a parameter, e.g."""
import my_utils
print("Average is", my_utils.average([10,23,30]))
print("Another average is", my_utils.average([10.2, 8.8, 2.6]))


# Methods of importing
"""Update the previous program utils_test.py, so that the import statement
explicitly imports the average() function directly into the program’s symbol table, allowing
the prefix to be removed from the later function calls."""
from my_utils import average
print(average([5,2,1]))
