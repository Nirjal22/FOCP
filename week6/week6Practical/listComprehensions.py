"""Write some code that uses a list comprehension to create a list called cubes that
contains the cubed values (x * x * x) of the numbers from 2 to 20 inclusive."""
cubes = [x**3 for x in range(2, 21)]
print(cubes)


"""Examine the above code and work out which user names will be placed in the
some_users list. What is the condition that has to be met for inclusion?"""
# Example list of user names
all_users = ["Nirjal", "Ritik", "Rashmi", "Priyanka", "Prateek", "Abhishek"]

# Fix the line of code
some_users = [u for u in all_users if len(u) < 8]

# Display the result
print(some_users)

