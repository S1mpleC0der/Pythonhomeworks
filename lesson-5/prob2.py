def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"Year {year}: ${amount:.2f}")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of return: "))
years = int(input("Enter the years: "))
print()
invest(principal, rate, years)


