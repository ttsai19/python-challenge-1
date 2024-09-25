# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

# Initialize an empty order list to store customer's order
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to view different sections of the menu, so let's create a continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            item_map = {}
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        item_map[item_counter] = (f"{key} - {key2}", value2)
                        item_counter += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    item_map[item_counter] = (key, value)
                    item_counter += 1

            print(menu_dashes)

            # Prompt the customer to select an item from the menu
            menu_selection = input("Please enter the number of the item you want to order: ")

            # Validate the input for menu selection
            if not menu_selection.isdigit():
                print("Error: Please enter a valid number.")
            else:
                menu_selection = int(menu_selection)
                if menu_selection not in item_map.keys():
                    print("Error: Item number not found.")
                else:
                    # Get the item name and price from item_map
                    item_name, item_price = item_map[menu_selection]

                    # Ask the customer for the quantity of the selected item
                    quantity = input(f"How many {item_name}(s) would you like? (default 1): ")

                    # Validate the quantity input
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                    print(f"{quantity} x {item_name}(s) added to your order.")

                    # Ask the customer if they would like to keep ordering
                    while True:
                        continue_ordering = input("Would you like to order more items? (y/n): ").lower()

                        match continue_ordering:
                            case 'y':
                                break
                            case 'n':
                                print("Thank you for your order.")
                                print("Here's your receipt:")
                                print(f"{'Item name':<30}{'Price':<10}{'Quantity':<10}")
                                print("-" * 50)

                                # Step 6: Create a for loop to loop through the order list
                                for order in order_list:
                                    # Step 7: Inside the loop, save the value of each key as their own variable
                                    item_name = order['Item name']
                                    price = order['Price']
                                    quantity = order['Quantity']

                                    # Step 8: Calculate the number of empty spaces for formatting
                                    num_item_spaces = 30 - len(item_name)
                                    price_spaces = " " * (10 - len(f"${price:.2f}"))
                                    quantity_spaces = " " * (10 - len(str(quantity)))

                                    # Step 9: Create space strings for formatting
                                    item_spaces = " " * num_item_spaces

                                    # Step 10: Print the receipt line
                                    print(f"{item_name}{item_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

                                # Step 11: Calculate the total price using list comprehension
                                total_price = sum(order['Price'] * order['Quantity'] for order in order_list)
                                print(f"{'-' * 50}\nTotal Price: ${total_price:.2f}")
                                exit()
                            case _:
                                print("Invalid input, please enter 'y' or 'n'.")
        else:
            # Tell the customer they didn't select a valid menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
