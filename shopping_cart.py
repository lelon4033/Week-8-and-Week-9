
#create  a shopping cart program that will continously ask the user for a food product and the price of that product.
# have an exit clause if the user wishes to adding more things to their cart.
# at the end show the food items and the total cost to the user.

foods = []
prices = [] 
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}:R "))
        foods.append(food)
        prices.append(price)
        
        print("-------------------your cart-------------------")
        
        for food in food:
            print(food, end=", ")
            
        for price in prices:
            total += price
            
            print("/n")
            print(f"your total is: R{total}")
        