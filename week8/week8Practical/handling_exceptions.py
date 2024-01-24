"""write a small program that opens the info.txt file, then reads and displays each
line of text using a for...in loop. Rather than explicitly call the close() method, use the
‘with’ statement to wrap the file handling code."""
with open("info.txt","r") as file:
    for lines in file:
        print(lines)
