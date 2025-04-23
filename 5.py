def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

while True:
    try:
        print("\n--- Factorial Calculator ---")
        print("1. Compute Factorial")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Factorial is not defined for negative integers.")
            else:
                fact = factorial(num)
                print(f"Factorial of {num} is {fact}")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input! Please enter an integer.")
