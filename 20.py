class InsufficientFunds(Exception):
    pass

class InvalidAccountNumber(Exception):
    pass

accounts = {
    "12345": 1000,
    "67890": 500
}

def withdraw(account_number, amount):
    if account_number not in accounts:
        raise InvalidAccountNumber("Account number does not exist.")
    
    if accounts[account_number] < amount:
        raise InsufficientFunds("Not enough balance to withdraw.")
    
    accounts[account_number] -= amount
    print(f"Withdrawal successful. Remaining balance: {accounts[account_number]}")

# Sample usage
try:
    acc_no = input("Enter your account number: ")
    amt = float(input("Enter the amount to withdraw: "))
    withdraw(acc_no, amt)
except (InvalidAccountNumber, InsufficientFunds) as e:
    print("Transaction failed:", e)
