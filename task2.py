stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150,
    "NFLX": 400
}

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================\n")

total_investment = 0

portfolio_details = ""

num_stocks = int(input("How many stocks do you want to add? : "))

for i in range(num_stocks):

    print(f"\nEnter Details for Stock {i + 1}")

    stock_name = input("Enter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock_name in stock_prices:

        stock_price = stock_prices[stock_name]

        investment_value = stock_price * quantity

        total_investment += investment_value

        print("\n------ Stock Summary ------")
        print("Stock Name       :", stock_name)
        print("Price Per Share  :", stock_price)
        print("Quantity         :", quantity)
        print("Investment Value :", investment_value)

        portfolio_details += (
            f"Stock Name       : {stock_name}\n"
            f"Price Per Share  : {stock_price}\n"
            f"Quantity         : {quantity}\n"
            f"Investment Value : {investment_value}\n"
            f"-----------------------------\n"
        )

    else:
        print("\nStock not available in database!")

print("\n===================================")
print("      PORTFOLIO SUMMARY")
print("===================================")

print(f"Total Investment Value : {total_investment}")

file = open("portfolio_report.txt", "w")

file.write("===================================\n")
file.write("       STOCK PORTFOLIO REPORT\n")
file.write("===================================\n\n")

file.write(portfolio_details)

file.write(f"\nTotal Investment Value : {total_investment}")

file.close()

print("\nPortfolio report saved successfully!")
print("File Name : portfolio_report.txt")