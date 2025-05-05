username="shap"
password="123"

input_user=input("Enter your username:")
input_pass=input("Enter password:")

if input_user==username and input_pass==password:
    print("Login Successful!\n")

while True:
    print("\n======= MENU =======")
    print("1.create account") 
    print("2.deposit money")
    print("3.withdraw money")
    print("4.check balance")
    print("5.Transaction history")
    print("6.exit")

def creat_account():
    global account
    name= input("enter account hold name:")
    try:
        balance=float(input("Enter balance:"))
        if balance<0:
            print("Balance is not found.")
            return
    except ValueError:
        printI("Invalid ammount!")

acc_no=str(next_acc_no)
next_acc_no+=1
account[acc_no]={
    "name":name,
    "balance":balance,
    "transation":[f"initial deposit{balance}"]
}

save_data()
print(f"Account created successfully! Account number:")

choice=int(input("Enter your choice:"))
if choice==1:
    print("new account.")
elif choice==2:
    deposit=float(input("Enter amount to deposit:"))
    account_balance=account_balance+deposit
    print("Deposit sucessfully!.New balance:",account_balance)
elif choice==3:
    amount=float(input("Enter amount to withdraw:"))
    if account_balance>=amount:
        account_balance=account_balance-amount
        print("Successfully d")



















######## Deposit ########
def deposit():
    acc_no=input("Enter Account number:")
    if acc_no not in accounts:
        print("Account is not found")
        return
    try:
        amount=float(input("Enter amount:"))
        if amount<=0:
            print("Amount must be positive." )
            return
        accounts+=amount
        accounts.append(f"deposit amount:")

        print(" Successfully.")
    except:
        print("invalid Amount")


########## withdraw #########

def withraw():
    acc_no=input("Enter account number:")
    if acc_no not in account:
        print('Account not found')
        return
    try:
        amount=float(input("Enter amount:"))
        if amount<=0:
            print("Amount must be positive.")
            return
        if amount> accounts:
            print('')





# choice=input("Enter Your choice(1-6):")

# try:
#     if choice=="1":
      

























# def create_account():
#     account_number=int(input("Enter account_number"))
#     account_hold_name=input("Enter name")
#     Balance=500000
#     print("account_number")
#     print("name")



                    
