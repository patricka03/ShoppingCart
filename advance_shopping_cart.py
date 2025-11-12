# Advanced shopping cart

shopping_cart = {}

while True:
    print("-----Shopping cart-----")
    print("Enter 1 if you’d like to add to your shopping cart: ")
    print("Enter 2 if you’d like to remove an item from your shopping cart: ")
    print("Enter 3 if you’d like to update an items in your shopping cart: ")
    print("Enter 4 if you’d like to view all item in your shopping cart: ")
    print("Enter 5 if you’d like to quit")

    choice = input("Choose an option (1-5): ")
    if choice == "5":
        break
    elif choice == "1":
        food = input("Enter the item that you will like to add: ")
        price = float(input("Enter the price of the item: "))
        shopping_cart[food] = price
        print(f"{food} has been added to your shopping cart")
    elif choice == "2":
        food = input("Enter the food you will like to remove: ")
        if food in shopping_cart:
            del shopping_cart[food]
            print(f"You have removed {food} from your shopping cart")
        else:
            print(f"The item: {food} you entered is not in your shopping cart")
    elif choice == "3":
        food = input("Enter the item you will like to update: ")
        if food in shopping_cart:
            price = float(input(f"Enter the new price for {food}: £"))
            shopping_cart[food] = price
            print("Your cart has now been updated")
        else:
            print(f"The item: {food} you entered is not in your shopping cart")
    elif choice == "4":
        print("\n-----Shopping cart-----")
        total = 0
        for food, price in shopping_cart.items():
            print(f"{food}: £{price}")
            total += price
        print(f"Total: £{total}")
    else:
        print("Invalid option. Please choose between 1 and 5.")