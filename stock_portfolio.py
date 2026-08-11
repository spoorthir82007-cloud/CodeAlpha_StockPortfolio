prices = {
"AAPL": 180,
"MSFT": 400,
"GOOGL": 150,
"AMZN": 200,
"TSLA": 250
}

print("Stock Portfolio Tracker")
print("======================")

total = 0

stock1 = input("Enter first stock symbol: ").upper()
quantity1 = int(input("Enter quantity: "))

price1 = prices.get(stock1, 0)
investment1 = quantity1 * price1
total = total + investment1

print(stock1, ":", quantity1, "shares =", investment1)

stock2 = input("Enter second stock symbol: ").upper()
quantity2 = int(input("Enter quantity: "))

price2 = prices.get(stock2, 0)
investment2 = quantity2 * price2
total = total + investment2

print(stock2, ":", quantity2, "shares =", investment2)

print()
print("======================")
print("Total Investment: $", total)
print("Thank you for using Stock Portfolio Tracker!")
