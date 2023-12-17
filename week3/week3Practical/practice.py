"""TASK: Input code containing a for loop that iterates over a list of numbers, printing a
running total during each iteration."""
numbers = [1,2,3,4,500,67,8,99]
for z in numbers:
    print(z)

"""TASK: Amend your previous solution so that if any value within the list is found to be over
100 then the loop should break immediately."""
for a in numbers:
    if a <100:
        print(a)
    else:
        break

"""TASK: Amend your previous solution once again, so that the message “all numbers
processed” is printed when the loop completes, but only if all values were less or equal to
100 (i.e. the loop did not break early)"""
for b in numbers:
    if b >100:
        print(f"value{b} is over 100. Breaking the loop.")
    else:
        print("All numbers processed")

