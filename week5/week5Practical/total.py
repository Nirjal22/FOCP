"""Improve the previous program by adding additional code that not only prints the total
of any passed arguments, but also calculates and prints the average. Execute the program
several times for testing. What happens if no arguments are passed?"""
import sys

count = len(sys.argv)
total = 0

if count > 1:
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

    average = total / (len(sys.argv) - 1)
    print("Total is", total)
    print("Average is", average)
else:
    print("no arguments were passed.")

