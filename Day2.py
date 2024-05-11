print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
while tip not in [10, 12, 15]:
    print("Tip must be 10, 12, or 15")
    tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
n = int(input("How many people are splitting the bill? "))
print(f"Each person should pay: ${round((bill+bill*(tip/100))/n,2)}")

