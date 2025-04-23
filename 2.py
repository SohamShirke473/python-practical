try:
    bs=float(input("Enter the Basic Salary :"))
    da=0.7*bs
    ta=0.3*bs
    hra=0.1*bs
    gross_salary = bs + da + ta + hra
    print(f"Basic Salary (BS): ₹{bs:.2f}")
    print(f"Dearness Allowance (DA - 70%): ₹{da:.2f}")
    print(f"Travel Allowance (TA - 30%): ₹{ta:.2f}")
    print(f"House Rent Allowance (HRA - 10%): ₹{hra:.2f}")
    print(f"Gross Salary: ₹{gross_salary:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for salary.")
