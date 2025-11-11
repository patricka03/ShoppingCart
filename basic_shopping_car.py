# Basic Shopping cart feature

foods = []
prices = []
total = 0

while True:
    food = input(f"Enter the food you would like to add to your shopping cart (q to quit): ")
    if food.lower() ==  "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: £"))
        foods.append(food)
        prices.append(price)

print("-----SHOPPING CART-----")

for food in foods:
    print(food)

for price in prices:
    total += price
print(f"Your total is: £{total}")
