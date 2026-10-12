
balance = int(input("Enter the balance first: "))
n = int(input("No. of operation."))
for i in range(n):
    amt = int(input())
    if amt % 100 == 0 and amt <= balance:
        balance -= amt
        print("SUCCESS")
    else:
        print("FAILED")

print(balance)