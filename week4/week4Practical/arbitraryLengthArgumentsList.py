"""Enter the example function shown above, then try calling it several times, passing a
different number of numeric arguments each time."""
def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)
print(calcAve(8))
print(calcAve(2,10))
