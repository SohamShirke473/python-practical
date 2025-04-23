numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nNumbers entered:", numbers)

total = sum(numbers)
print("Sum of the numbers:", total)

largest = max(numbers)
print("Largest number:", largest)
