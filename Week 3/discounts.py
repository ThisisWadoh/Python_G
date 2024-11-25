def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100)*price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Acquiring User Inputs
price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount_percent: "))

# Calculating Final Price
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount is: sh.{final_price: .2f}")

else:
    print(f"No discount applied. Final price is: sh.{price: .2f}")

    