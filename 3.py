"""Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following: D
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500"""

print("\nD : deposit"
      "\nW : Withdraw"
      "\nY : Exit Transaction")
print("<<----------------------------------->>")

Balance = 0
while True:
    transaction = (input("Enter Tansaction : "))
    if transaction == "Y":
        break
    
    else:
        transaction = transaction.split(" ")
        if transaction[0] == "D":
            Balance = Balance + int(transaction[1])        
        elif transaction[0] == "W":
            Balance = Balance - int(transaction[1])

if(Balance < 0):
    print("Insufficient Funds!!!!")
else:
    print("Balance : " , Balance)