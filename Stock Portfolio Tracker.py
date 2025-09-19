# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2700, "MSFT": 310, "AMZN": 3300}

# Get number of stocks to input
n = int(input("How many stocks do you want to enter? "))

portfolio = {}

# Input stock names and quantities
for i in range(n):
    stock = input(f"Enter stock name #{i+1}: ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity

# Calculate total investment
total_investment = 0
print("\n--- Portfolio Details ---")
for stock, quantity in portfolio.items():
    price = stock_prices.get(stock, 0)
    value = price * quantity
    total_investment += value
    print(f"{stock}: Quantity={quantity}, Price={price}, Value={value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: save to file
save = input("Do you want to save the result to portfolio.txt? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("--- Portfolio Details ---\n")
        for stock, quantity in portfolio.items():
            price = stock_prices.get(stock, 0)
            value = price * quantity
            file.write(f"{stock}: Quantity={quantity}, Price={price}, Value={value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")
