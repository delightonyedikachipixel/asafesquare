def calculate_discount(item_name, item_price, promotional_code):
    if promotional_code == "SAVE10":
        discount = 0.10 * item_price
    elif promotional_code == "HALFOFF":
        discount = 0.50 * item_price
    else:
        print(f"{promotional_code} is not a valid promotional code.")
    return item_price - discount
    
