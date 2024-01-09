"""Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']."""
def fun(entered_values):
    storing_in_list = list(set(entered_values))
    storing_in_list.sort()
    return storing_in_list
if __name__=="__main__":
    entered_values = input("Enter the values: ")
    print(fun(entered_values))
