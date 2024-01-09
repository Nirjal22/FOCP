"""One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes."""
def frequency_analysis(msg):
    # Initialize an empty dictionary to store letter frequencies
    let_cts = {}

    # Process each character in the message
    for char in msg.lower():
        if char.isalpha():  # Consider only alphabetic characters
            if char in let_cts:
                let_cts[char] += 1
            else:
                let_cts[char] = 1

    # Sort the dictionary based on letter counts in descending order
    std_cts = sorted(let_cts.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their counts
    print("Six most common letters and their counts:")
    for i in range(min(6, len(std_cts))):
        print(f"{std_cts[i][0]}: {std_cts[i][1]}")

if __name__ == "__main__":
    msg = input("Enter the encrypted message: ")
    frequency_analysis(msg)
