"""Enter the example function shown above, then try calling it using the keyword
arguments in several different orders."""
def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)
someFunc(1,2,3)
someFunc(y=2, z=3, x=1)
someFunc(y=2, z=3, x=1)


"""The built-in print() function supports a keyword argument called sep. This is used
to decide what character to display between each of the provided positional parameters.
Write some code that makes several calls to the print() function while setting the sep
argument to values other than a space (which is the default)."""
# Using different sep values in print function
print("Hello", "World", sep='-')  # Hello-World
print("One", "Two", "Three", sep=', ')  # One, Two, Three
print("Apple", "Orange", "Banana", sep='\t')  # Apple	Orange	Banana

