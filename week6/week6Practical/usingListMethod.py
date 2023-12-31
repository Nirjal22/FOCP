"""Write a for..in loop that iterates over all the elements of the squares list and
prints the square root of each to the screen. Hint: you may want to import a function from
the math module to help achieve this"""
import math
squares = [4,9,16,25]
for i in squares:
    print(math.sqrt(i))


"""Write some code that uses the append() method to add the next three square
values (49, 64, 81) to the end of the squares list."""
for j in range(7,10):
    squares.append(j**2)
print(squares)


"""Write some code that uses the extend() method to add the next three square
values, starting at 121 (11 x 11), to the end of the squares list."""
squares.extend([121, 144, 169])
print(squares)

"""Write some code that uses the insert() method to insert the value 2, to the very
beginning of the squares list."""
squares[0:0]=[2]
print(squares)

"""Write some code that uses the remove() method to remove the value 49 from the
squares list. Print the list afterwards to ensure the value has indeed been removed."""
squares.remove(49)
print(squares)


"""Write some code that uses the remove() method to remove the value 3 from the
squares list. Notice how an error is generated since the given value was not present."""
for a in squares.copy():
    if math.sqrt(a) == 3: 
        squares.remove(a)
print(squares)


""" Create a simple list that contains the values [1, 2, 3, 1, 2] and then use the
remove () method to remove the value 2. Which value is removed?"""
simple_list = [1,2,3,1,2]
simple_list.remove(2)
print(simple_list)
# The first value is removed.
