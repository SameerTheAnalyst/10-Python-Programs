print("Welcome to the tip calculator!")
bill = float(input("\nWhat was the total bill?: $"))
people = int(input("\nHow many people to split the bill?: "))
percentage_tip = int(input("\n What percentage of tip would you like to give?(don't add % sign): "))
total_bill = float(percentage_tip / 100 * bill + bill)
result = total_bill / people
print(f"\nEach person should pay: {result}")