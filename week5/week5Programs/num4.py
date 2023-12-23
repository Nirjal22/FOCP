"""Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend."""
import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx status codes)
        print(f"Website at {url} is reachable. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        print("Website may be unreachable or not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        check_website(url)
