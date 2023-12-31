"""Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers."""
def prime_num(number):
    if number >1:
        for i in range(2,int(number/2)+1):
            if number % i ==0:
                print(f"{number} is not prime number.")
                break
        else:
            print(f"{number} is a prime number.")
    else:
        print("Enter value greater than 1.")
number = int(input("Enter the number: "))
print(prime_num(number))
