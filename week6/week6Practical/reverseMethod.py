"""Write some code that uses the reverse() method to reverse the values of the
squares list. Print the list afterwards to ensure the values have been reversed."""
squares = [4,9,16,25]
squares.reverse()
print(squares)


"""Write some code that finds the index of the colour blue."""
colors = ["red", "green", "yellow", "blue", "red"]
print(colors.index("blue"))


""" Write some code that makes a copy of the colours using the copy() method.
Then make some changes to the original list. Print the contents of the copied list to ensure
these changes have not affected the copy."""
new_colors  = colors.copy()
colors  = ["red", "green", "yellow", "blue", "red","black"]
print(new_colors)
