def calculate_total_price(number_of_pizzas, is_tuesday, use_app, requires_delivery):
    try: #exceptional handling
        updated_price = pizza_cost_integer * number_of_pizzas
        if is_tuesday.lower() == 'y':
            # Apply Tuesday discount
            updated_price *= Tuesday_discount
        if number_of_pizzas >= 5 and not is_tuesday.lower() == 'y':
            # Free delivery for 5 or more pizzas on non-Tuesday
            updated_price += 0
        else:
            # Apply delivery cost
            updated_price += delivery_cost if requires_delivery.lower() == 'y' else 0
        if use_app.lower() == 'y':
            # Apply BPP App discount
            updated_price *= 0.75
        return updated_price #returns the final output 
    except ValueError:
        print("Please enter a valid number.")
        return None

if __name__ == "__main__":
    print("BPP Pizza Price Calculator\n==========================\n")
    # Creating Global variable
    pizza_cost = u'\u00a312'  # This is used to write a unicode string.
    # To display the price of pizza
    print(f"The cost of Pizza is {pizza_cost}")
    # Remove the pound sign and convert to an integer
    pizza_cost_integer = int(pizza_cost[1:])
    # The given values
    Tuesday_discount = 0.50
    delivery_cost = 2.50
    BPP_App = 0.25
    
    number_of_pizzas = 0
# while True is used to continue the loop until the user input the valid input.
    while True:
        try:
            checking_number_of_pizzas = int(input("How many pizzas ordered?: "))
            if checking_number_of_pizzas > 0:
                number_of_pizzas = checking_number_of_pizzas
                break
            else:
                print("Invalid input! Please enter a positive value.")
        except ValueError:
            print("Enter a valid integer.")
# for delivery
    delivery = input("Is delivery required? (Y/N): ").lower() #lower() is used to change the entered input in lowercase.
    while delivery not in ('y', 'n'):
        print("Invalid Input! Please enter 'y' or 'n'.")
        delivery = input("Is delivery required? (Y/N): ").lower()
    requires_delivery = delivery
# for tuesday
    tuesday = input("Is it Tuesday?(Y/N): ").lower()
    while tuesday not in ('y', 'n'):
        print("Invalid Input! Please enter 'y' or 'n'.")
        tuesday = input("Is it Tuesday?(Y/N): ").lower()
    is_tuesday = tuesday
# for app
    app = input("Are you using App?(Y/N): ").lower()
    while app not in ('y', 'n'):
        print("Invalid Input! Please enter 'y' or 'n'.")
        app = input("Are you using App(Y/N): ").lower()
    use_app = app
# calling the function
    total_price = calculate_total_price(number_of_pizzas, is_tuesday, use_app, requires_delivery)
    if total_price is not None: #if the value is not none then it prints the final result.
        print(f"Total Price: \u00a3{total_price:.2f}")
