def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

try:

    principal = float(input("Enter the Principal amount: "))
    rate = float(input("Enter the Rate of Interest (%): "))
    time = float(input("Enter the Time (in years): "))


    interest = calculate_simple_interest(principal, rate, time)


    print(f"\nSimple Interest = ₹{interest:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
