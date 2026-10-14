# Calculate food bill with 18% GST
def calculateFoodBill(a, b):
    # Add both food item amounts
    amount = a + b

    # Calculate 18% GST
    gst = amount * 18 / 100

    # Return amount including GST
    return amount + gst


# Calculate room bill with 12% GST
def calculateRoomBill(c, d):
    # Add both room charges
    amount = c + d

    # Calculate 12% GST
    gst = amount * 12 / 100

    # Return amount including GST
    return amount + gst


# Calculate service charge with 5% GST
def calculateServiceCharge(e):
    # Calculate 5% GST
    gst = e * 5 / 100

    # Return amount including GST
    return e + gst


# Calculate total hotel bill
def totalBill(a, b, c, d, e):
    food = calculateFoodBill(a, b)
    room = calculateRoomBill(c, d)
    service = calculateServiceCharge(e)

    # Add all amounts after GST
    return food + room + service


# Calculate discount and final bill
def calculateDiscountedBill(a, b, c, d, e):
    # Get total bill after GST
    total = totalBill(a, b, c, d, e)

    # Calculate 10% discount
    discount = total * 10 / 100

    # Subtract discount
    payable = total - discount

    # Print results
    print(f"Total after GST = {total:.2f}")
    print(f"Discount = {discount:.2f}")
    print(f"Final payable amount = {payable:.2f}")

    # Return final amount
    return payable


# Pass sample values directly
calculateDiscountedBill(100, 100, 100, 100, 100)