"""Write a small program that opens the "info.txt" file in append (a) mode. Use the
write() method to add an extra line of text saying "this is an extra line".
Remember to close the file once the content has been read. Open the file with a text editor
and examine the contents."""
file = open("info.txt","a")
file.write("this is an extra line")
file.close()
