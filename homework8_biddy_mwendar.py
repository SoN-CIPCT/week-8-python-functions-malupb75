# ---------------------------------------------------
# File: homework8_biddy_mwendar.py
# ---------------------------------------------------
# Part 1: Function Definition
# ---------------------------------------------------

def make_sandwich(*ingredients):
    """
    Accepts multiple sandwich ingredients and prints a summary of the sandwich order.
    """
    if not ingredients:
        print("\nYou didn't add any ingredients. Please choose at least one ingredient for your sandwich!\n")
        return
    
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("Your sandwich is ready!\n")

# ---------------------------------------------------
# Part 2: Function Calls (Testing the Function)
# ---------------------------------------------------

# First sandwich order with 4 ingredients
print("="*50)
print("Order 1: Whole Wheat Roast Beef Sandwich")
print("="*50)
make_sandwich("Whole wheat bread", "Roast beef", "Bacon", "Tomato slices")

# Second sandwich order with 6 ingredients
print("="*50)
print("Order 2: Veggie Hummus Wrap")
print("="*50)
make_sandwich("Tortilla", "Hummus", "Spinach", "Cucumber", "Red onion", "Bell peppers")
