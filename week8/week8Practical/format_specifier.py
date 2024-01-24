"""Rewrite your earlier code that displayed the area of a rectangle, but include a format
specifier that limits the displayed result to three decimal places."""
# Define the width and height of the rectangle
width = 104.32
height = 15.654
print(f"The area of a rectangle with a width of {width} and a height of {height} is {width * height:.3f}.")



"""Try setting the name and age variables to different values and executing the above
print() statement multiple times. Notice the alignment and column width enforced due to
the print specifier."""
name  = "Ritik"
age = 20
print(f"{name:15} - {age:10}")



"""Write a print() statement that displays the name and age values, with a column
width of 20 for each, both right aligned, and with the age being shown to two decimal
places. The fill character should be a dollar symbol $."""
print(f"{name:$>20} - {age:$>20.2f}")


