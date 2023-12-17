"""Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""
def centi(temp):
    temp = float(temp) # changing string to float
    fahrenheit = temp *(9/5)+32 #formula
    print(f"The temperature in fahrenheit is: {fahrenheit}F.") #output
temperature = (input("Enter the temperature in celcius: "))
temp = temperature[:-1] 
try:
    if temperature[-1] == 'C':
        centi(temp)
    else:
        print("Invalid input! Enter capital c i.e 'C'")
finally:
    print("Program Complete.")
