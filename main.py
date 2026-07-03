pizza_cost = int(input("how much does 1 pizza cost? "))
cash = int(input("how much cash do you have? "))

if pizza_cost <= 0:
    print("pizza cost must be more than 0")
elif cash < pizza_cost:
    print("you can't afford to buy a pizza.")
else:
    pizza_quantity = cash // pizza_cost
    change = cash % pizza_cost
    print(f"you can afford to buy {pizza_quantity} pizzas.")
    print(f"your change will be £{change}")

