"""Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument)."""
import sys

def report_argument_count():
    # Subtract 1 to exclude the program name itself
    argument_count = len(sys.argv) - 1
    print(f"Number of command-line arguments: {argument_count}")

if __name__ == "__main__":
    report_argument_count()

