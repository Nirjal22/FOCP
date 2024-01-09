"""Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on."""
def manage_countries():
    countries_capitals = {}

    while True:
        country_name = input("Enter the name of a country (or 'exit' to terminate): ").lower()

        if country_name == 'exit':
            break

        if country_name in countries_capitals:
            print(f"The capital of {country_name.capitalize()} is {countries_capitals[country_name]}")
        else:
            capital_city = input(f"Enter the capital city of {country_name.capitalize()}: ")
            countries_capitals[country_name] = capital_city
            print(f"Added {country_name.capitalize()} with capital {capital_city}")

if __name__ == "__main__":
    manage_countries()
