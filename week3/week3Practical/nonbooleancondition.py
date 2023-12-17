"""TASK: Rewrite the above code that inputs a name then prints a message, but change the
condition so it explicitly uses a Boolean expression. Use the example below to help."""
name = input("Enter your name: ")
if len(name)>0:
    print("Your name is", name)
else:
    print("Name not entered")