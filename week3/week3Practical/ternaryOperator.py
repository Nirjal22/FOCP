# TASK: Rewrite the code shown below as a single line Ternary expression.
age = int(input("Enter the age: "))
print("you are an adult") if age >= 18 else print("you are not an adult, yet!")

# Using while and for loops

"""TASK: Input and execute a for loop that iterates over a list of four names, printing each of
them to the screen"""
names = ["Nirjal","Roshan","Prasanna","Aniket"]
for i in names:
    print(i)

# Range() function
""""TASK: Input and execute a for loop that uses a range() function to generate the following
output:"""
num = int(input("Enter the range: "))
for j in range(2, num+2, 2):  # Adjust the range to include even numbers up to num*2
    result = j**j
    print(f"{j} to the power of {j} = {result}")

# using break and continue

"""TASK: Input code containing a for loop that iterates over a list of numbers, printing a
running total during each iteration."""
numbers = [1,2,3,4,500,67,8,99]
for z in numbers:
    print(z)

"""TASK: Amend your previous solution so that if any value within the list is found to be over
100 then the loop should break immediately."""
for a in numbers:
    if a <=100:
        print(a)
    else:
        break

"""TASK: Amend your previous solution once again, so that the message “all numbers
processed” is printed when the loop completes, but only if all values were less or equal to
100 (i.e. the loop did not break early)"""
for b in numbers:
    if b <=100:
        print(b)
    else:
        break
print("All values processed")
