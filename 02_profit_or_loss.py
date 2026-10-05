# Program 2: Calculate Profit or Loss

cost_price = 500
selling_price = 650

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No Profit, No Loss")
