"""Define a function that takes two numeric values, multiplies them together then returns
the result. If the function is called with only a single argument however, then the value should
be multiplied by itself. Once the function is defined, call it several times and display the
returned values for testing purposes."""
def multiply_values(a, b=None):
    if b is None:
        result = a * a
    else:
        result = a * b
    return result

# Test the function with different argument values
result1 = multiply_values(5, 3)
print("Result 1:", result1)

result2 = multiply_values(4)
print("Result 2:", result2)

result3 = multiply_values(2.5, 2)
print("Result 3:", result3)
