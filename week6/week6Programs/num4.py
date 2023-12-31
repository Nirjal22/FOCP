"""Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way."""
def entered_str(values):
    b = []
    for i in values:
        b.append(i)
    c = b[::-1]
    d = ' '.join(c)
    e = d.replace(" ","")
    return e
if __name__=="__main__":
    values = str(input("Enter the message: \n"))
    print(entered_str(values))
