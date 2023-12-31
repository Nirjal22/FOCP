"""Create a tuple called address that includes your own “house number”, “street” and,
“postcode” as three different values."""
address = ("123","7-calif","44100")
print(type(address))

"""Try entering the above examples to create single element tuples. Then use the
type() function to examine the data-type of the created variables"""
the_one = ("Neo",)
print(type(the_one))


# Sequence Unpacking
"""Use sequence unpacking to extract the values you stored within the address tuple
earlier. Unpack the tuple into variables named house_num, street and postcode."""
(house_num , street , postcode) =  address
print(house_num)
print(street)
print(postcode)



"""Write some code that calls the print() function to output the contents of the
address tuple you created earlier. Ensure you use the ‘*’ prefix so that the elements are
extracted before being passed to the function. Compare this with a version of the same code
that calls the print() function without using the ‘*’ prefix,"""
address = ("123", "7-calif", "44100")

# Using '*' prefix to unpack the tuple elements before passing to the print function
print(*address)
