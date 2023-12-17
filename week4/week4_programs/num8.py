"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""

def six_temp(nums):
    maximum = max(nums)
    print(f"The maximum temperature is: {maximum}C")
    minimum = min(nums)
    print(f"The minimum temperature is: {minimum}C")
    mean = sum(nums)/6
    print(f"The mean of these temperature is: {mean}")

def main():
    nums=[]
    for i in range(6):
        value=input("Enter " + str(i+1) + " temperature: ")
        if(value==""):
            exit()
        value=float(value[:-1])
        nums.append(value)
    six_temp(nums)

main()