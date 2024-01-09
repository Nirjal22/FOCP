"""Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line."""
def fun1(entered_str1,entered_str2):
    return sorted(set(entered_str1) | set(entered_str2))
def fun2(entered_str1,entered_str2):
    return sorted(set(entered_str1) & set(entered_str2))
def fun3(entered_str1,entered_str2):
    return sorted((set(entered_str1) | set(entered_str2)) - (set(entered_str1) & set(entered_str2)))

if __name__ == "__main__":
    entered_str1 = input("Enter the first string: ")
    entered_str2 = input("Enter the second string: ")
    print(fun1(entered_str1,entered_str2), fun2(entered_str1,entered_str2),fun3(entered_str1,entered_str2))
