"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them."""
import sys

def find_shortest_argument():
    # Exclude the program name itself
    arguments = sys.argv[1:]

    if not arguments:
        print("No arguments provided.")
        return

    shortest_argument = min(arguments, key=len)
    print(f"Shortest command-line argument: {shortest_argument}")

if __name__ == "__main__":
    find_shortest_argument()
