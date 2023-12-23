"""Open the first_prog.py and add some extra code that identifies and prints a
message stating whether the entered number is divisible by 10. You should be able to base
the new code on the if statement already provided. Once completed, save the file and
execute it again for testing."""
number = input("Enter a number: ")  # taking input from the user and storing the value in the variable 'number'
number = int(number)  # entered value is in string so changing it to an integer
print("The number entered was", number)  # print() function to give output

if (number % 2) == 0:  # condition using if statement
    print("That is an even number")
else:
    print("That is an odd number")

if (number % 10) == 0:  # check if the number is divisible by 10
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")

