"""Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!"""
def intoBinary(number):
    binary_number = ""
    if number > 0:
        while number >= 1:
            if number % 2 == 0:
                binary_number = "0" + binary_number
            else:
                binary_number = "1" + binary_number
            number //= 2
        return binary_number
    else:
        return "Invalid Input. Enter a positive integer."
# Get user input
number = int(input("Enter the number that you want to convert to binary: "))
# Call the function and print the result
result = intoBinary(number)
print(f"The binary representation of {number} is: {result}")
