# TASK: Use the built-in help() function to view all the methods available on the dict type.
# Then write some code that uses the popitem() method to remove some key:value pairs
# from the stock dictionary.



stock = {"apple": 20, "pear": 30, "banana": 15, "kiwi": 10, "orange": 25}


removed_item1 = stock.popitem()
print(f"Removed item 1: {removed_item1}")
removed_item2 = stock.popitem()
print(f"Removed item 2: {removed_item2}")

print(stock)
