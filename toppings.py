import re


requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print(f"Adding{requested_toppings[0]}")
elif 'extra cheese' in requested_toppings:
    print(f"Adding{requested_toppings[1]}")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni")

print("\nFinished making your pizza!")