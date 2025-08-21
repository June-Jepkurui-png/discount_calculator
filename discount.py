def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
    
    Returns:
        float: The final price after discount, or original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
