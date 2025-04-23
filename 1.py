def rupees_to_dollar(n):
    return n / 83  

def celsius_to_fahrenheit(n):
    return (n * (9 / 5)) + 32

try:
    print("Choose a converter:")
    print("1. Rupees to Dollar")
    print("2. Celsius to Fahrenheit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        amount = float(input("Enter amount in Rupees: "))
        converted = rupees_to_dollar(amount)
        print(f"{amount:.2f} INR = {converted:.2f} USD")

    elif choice == "2":
        temp = float(input("Enter temperature in Celsius: "))
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp:.2f}°C = {converted:.2f}°F")

    else:
        print("Invalid choice! Please enter 1 or 2.")

except ValueError:
    print("Invalid input! Please enter a numeric value.")
