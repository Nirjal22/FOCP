"""Write some code that uses the str.format() method to display the area of a circle
with a radius specified by the variable r. Use a keyword replacement field called area to
identify the calculated area and refer to this when passing the value to the str.format()
method. The output should look like the following, in the case where r is set to 52."""
import math
# Given radius
r = 52
# Calculate the area of the circle
area = math.pi * r**2
# Display the result using str.format()
output = "A circle with radius {} has an area of {:.13f}".format(r, area)
print(output)


"""Convert the f-string based statement below into an equivalent that uses the
str.format() method to generate the same output."""
name = "Nirjal"
age = 19
output = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(output)
