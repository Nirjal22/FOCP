"""Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program."""
def test(alpha):
    uppercase_count =0
    lowercase_count =0
    for char in alpha:
        if(char.isupper()):
            uppercase_count +=1
            # print(f"{alpha} is in upper case. The number of strings in uppercase is {uppercase_count}")
        else:
            lowercase_count +=1
            # print(f"{alpha} is in lower case. The number of strings in lowercase is {lowercase_count}")
    print(f"Number of Uppercase: {uppercase_count}, Number of lowercase: {lowercase_count}")
alpha=str(input("Enter the string: "))
print(test(alpha))
