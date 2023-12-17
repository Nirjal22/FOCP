"""1. Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function."""
def integer_range(num):
    if(num>0 and num<=100):
        return True
    else:
        return False
num=int(input("Enter the single integer: "))
print(integer_range(num))
