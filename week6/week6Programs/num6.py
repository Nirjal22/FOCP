"""""Write a program that decrypts messages encoded as above."""
import re
def fun(entered_val):
    return re.sub(r'xy','',entered_val)

if __name__=="__main__":
    print(fun(entered_val="sxyexynxyd cxyhxyexyexysxye"))
