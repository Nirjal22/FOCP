"""Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fifth character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye"""
def fun(entered_values):
    creating_list = list(entered_values)
    changing_to_string = ' '.join(creating_list)
    removing_Extra_spaces = changing_to_string.replace("  "," ")
    return removing_Extra_spaces

    
def fun1(entered_values):
    randomStringToInsert = 'xy'
    output=''
    stringToInsert=''
    for index,character in enumerate(entered_values):
        if character==' ' or index==len(entered_values)-1:
            stringToInsert=character
        else:
            stringToInsert=character+randomStringToInsert
        output+=stringToInsert
    return output

if __name__=="__main__":
    # entered_values = str(input("Enter the string: "))
    print(fun(entered_values = "send cheese"))
    print(fun1(entered_values = "send cheese"))
