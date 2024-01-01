def calculate_total_price(number_of_pizzas, is_tuesday, use_app, requires_delivery):
    try:
        if is_tuesday.lower() not in ('y', 'n'):
            print("Please enter the correct value 'y' or 'n'.")
            return None

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

        return updated_price

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
    checking_number_of_pizzas = int(input("How many pizzas ordered? "))
    while True:
        if checking_number_of_pizzas >= 0:
            number_of_pizzas = checking_number_of_pizzas
            break
        else:
            print("Invalid input! Please enter a non-negative value.")
            checking_number_of_pizzas = int(input("How many pizzas ordered? "))

    requires_delivery = input("Is delivery required? (Y/N): ").lower()
    is_tuesday = input("Is it Tuesday? (Y/N): ").lower()
    use_app = input("Did the customer use the app? (Y/N): ").lower()

    while requires_delivery not in ('y', 'n') or is_tuesday not in ('y', 'n') or use_app not in ('y', 'n'):
        print("Please input 'y' or 'n'.")
        requires_delivery = input("Is delivery required? (Y/N): ").lower()
        is_tuesday = input("Is it Tuesday? (Y/N): ").lower()
        use_app = input("Did the customer use the app? (Y/N): ").lower()

    total_price = calculate_total_price(number_of_pizzas, is_tuesday, use_app, requires_delivery)

    if total_price is not None:
        print(f"Total Price: \u00a3{total_price}")


