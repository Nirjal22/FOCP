"""Input the above function definition. Once that is done make several calls to the
function passing different argument values and displaying the returned value."""
def findMax(a,b):
# Finds the maximum of two values.
    if ( a > b ):
        max = a
    else:
        max = b
    return max
print(findMax(2,3))
print(findMax(5,2))
print(findMax(4,1))
