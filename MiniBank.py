# accounts = {}
# account_number_counter = 1000  
# users = {"admin": "password123"}  

# def create_account():
#     global account_number_counter
#     name = input("Enter name: ")
#     account_number = str(account_number_counter)  
#     accounts[account_number] = {
#         'name': name,
#         'balance': 0,
#         'transactions': []
#     }
#     print(f"Account successfully created!\nAccount Number: {account_number}")
#     account_number_counter += 1

# def deposit():
#     acc_no = input("Enter account number: ")
#     if acc_no in accounts:
#         try:
#             amount = float(input("Enter deposit amount: "))
#             if amount <= 0:
#                 print("Invalid amount! Must be greater than zero.")
#                 return
            
#             accounts[acc_no]['balance'] += amount
#             accounts[acc_no]['transactions'].append(f" - Deposit: {amount:.2f}")
#             print(f"Deposit successful! Current balance: {accounts[acc_no]['balance']:.2f}")
#         except ValueError:
#             print("Invalid amount! Enter a valid number.")
#     else:
#         print("Account not found.")

# def withdraw():
#     acc_no = input("Enter account number: ")
#     if acc_no in accounts:
#         try:
#             amount = float(input("Enter withdrawal amount: "))
#             if amount <= 0:
#                 print("Invalid amount! Must be greater than zero.")
#                 return
#             if amount > accounts[acc_no]['balance']:
#                 print("Insufficient balance!")
#                 return
            
#             accounts[acc_no]['balance'] -= amount
#             accounts[acc_no]['transactions'].append(f" - Withdrawal: {amount:.2f}")
#             print(f"Withdrawal successful! Remaining balance: {accounts[acc_no]['balance']:.2f}")
#         except ValueError:
#             print("Invalid amount! Enter a valid number.")
#     else:
#         print("Account not found.")

# def view_transactions():
#     acc_no = input("Enter account number: ")
#     if acc_no in accounts:
#         print(f"Transaction history for {accounts[acc_no]['name']} (Account No: {acc_no}):")
#         for transation in accounts[acc_no]['transactions']:
#             print(f"- {transation}")
#     else:
#         print("Account not found!")

# def user_login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username in users and users[username] == password:
#         print("Login successful!")
#     else:
#         print("Invalid credentials!")

# def check_balance():
#     acc_no = input("Enter account number: ")
#     if acc_no in accounts:
#         print(f"{accounts[acc_no]['name']}'s balance: {accounts[acc_no]['balance']}")
#     else:
#         print("Account not found")


# while True:
#     print("\nBanking System Menu:")
#     print("1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. View Transactions")
#     print("5.check balance")
#     print("6. User Login")
#     print("7. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         create_account()
#     elif choice == "2":
#         deposit()
#     elif choice == "3":
#         withdraw()
#     elif choice == "4":
#         view_transactions()
#     elif choice == "5":
#         check_balance()
#     elif choice == "6":
#         user_login()
#         break
#     elif choice == "7":
#          print("Exiting system... Thank you!")
    # else:
    #     print("Invalid choice! Please try again.")
 

def Admin():
    admin_name= input("Enter name:")
    admin_password= input("Enter password:")

    with open("admin.txt",'w')as file:
        file.write(f"{admin_name}/t{admin_password}/n")

    if admin_name and admin_password:
        print("Login successfully")
    else:
        print("Login failed")

Admin()

def customer():
    customer_name=input("Enter name:")
    customer_address=
    customer_pass=input("Enter password:")

    with open("customer.txt",'a')as file:
        file.write(f'{customer_name}/t{customer_pass}/n')

customer()

def save_transaction():
    acc_no=input("Enter account number:")
    
    with open("transactions.txt", "a") as file:  
        file.write(f"{acc_no}/t{save_transaction}\n")

save_transaction()

def user():
    user_name=input("Enter name:")
    user_password=input("Enter password:")

    with open("user.txt","a")as file:
        file.write(f"{user_name}/t{user_password}\n")
user()
                    
