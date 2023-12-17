"""Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean."""
def six_temp(temp1,temp2,temp3,temp4,temp5,temp6):
    #To find max
    maximum = max(temp1,temp2,temp3,temp4,temp5,temp6)
    print(f"The maximum temperature is: {maximum}C")
    #To find minimum
    minimum = min(temp1,temp2,temp3,temp4,temp5,temp6)
    print(f"The minimum temperature is: {minimum}C")
    #to find the mean
    mean = (temp1+temp2+temp3+temp4+temp5+temp6)/6
    print(f"The mean of these temperature is: {mean}")
tempA = input("Enter first temperature: ")
tempB = input("Enter second temperature: ")
tempC = input("Enter third temperature: ")
tempD = input("Enter fourth temperature: ")
tempE = input("Enter fifth temperature: ")
tempF = input("Enter sixth temperature: ")
try:
    if (tempA[-1]==tempB[-1]==tempC[-1]==tempD[-1]==tempE[-1]==tempF[-1]=='C'):
        temp1 = float(tempA[:-1])
        temp2 = float(tempB[:-1])
        temp3 = float(tempC[:-1])
        temp4 = float(tempD[:-1])
        temp5 = float(tempE[:-1])
        temp6 = float(tempF[:-1])
        six_temp(temp1,temp2,temp3,temp4,temp5,temp6)
    else:
        print("Invalid Input!")
finally:
    print("Program complete!")
