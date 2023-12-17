""" When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)"""
def entered_string(data):
    if(len(data)>1):
        return data[:-1]
    else:
        return data
data = str(input("Enter the data: "))
print(entered_string(data))
