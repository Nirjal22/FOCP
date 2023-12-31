"""Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original)."""
def factor_int(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Get user input
number = int(input("Enter the number that you want to factorize: "))

# Call the function and print the result
result = factor_int(number)
print(f"The factors of {number} are: {result}")
