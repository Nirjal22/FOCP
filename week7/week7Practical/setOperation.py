# TASK: Rewrite the previous code so that it checks that the input name is NOT within the set
# of known names. Hint: use the not in operator.



knownNames = {"John","Luffy","Trump","Naruto","Roman","Eren"}

input_name = input("Enter your name: ")

if input_name not in knownNames:
    print(f"You are not listed in the set of known names.")
else:
    print(f"You are listed in the set of known names.")
