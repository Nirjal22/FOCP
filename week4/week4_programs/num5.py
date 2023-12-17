"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""
def centigrade(temp):
    fahrenheit = temp *(9/5)+32
    print(f"The converted temperature of centigrade in fahrenheit is: {fahrenheit}")
    # print(fahren(fahrenheit)) 
    return fahren(fahrenheit) # we can do both.

def fahren(fahrenheit):
    celcius = (fahrenheit-32) * 5/9
    print(f"The converted temperature of fahrenheit in centigrade is: {celcius}")

temp = float(input("Enter the temperature in centigrade: "))
print(centigrade(temp))
