accounts = {}
account_number_counter = 1000
users = {"admin": "password123"}  

def create_account():
    global account_number_counter
    name = input("Enter name: ")
    account_number = str(account_number_counter)  
    accounts[account_number] = {
        'name': name,
        'balance': 0,
        'transactions': []
    }
    print(f"Account successfully created!\nAccount Number: {1000}")
    account_number_counter += 1

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Invalid amount! Must be greater than zero.")
                return
            
            accounts[acc_no]['balance'] += amount
            accounts[acc_no]['transactions'].append(f" - Deposit: {amount:.2f}")
            print(f"Deposit successful! Current balance: {accounts[acc_no]['balance']:.2f}")
        except ValueError:
            print("Invalid amount! Enter a valid number.")
    else:
        print("Account not found.")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid amount! Must be greater than zero.")
                return
            if amount > accounts[acc_no]['balance']:
                print("Insufficient balance!")
                return
            
            accounts[acc_no]['balance'] -= amount
            accounts[acc_no]['transactions'].append(f" - Withdrawal: {amount:.2f}")
            print(f"Withdrawal successful! Remaining balance: {accounts[acc_no]['balance']:.2f}")
        except ValueError:
            print("Invalid amount! Enter a valid number.")
    else:
        print("Account not found.")

def view_transactions():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print(f"Transaction history for {accounts[acc_no]['name']} (Account No: {acc_no}):")
        for transation in accounts[acc_no]['transactions']:
            print(f"- {transation}")
    else:
        print("Account not found!")

def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid credentials!")

def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        print(f"{accounts[acc_no]['name']}'s balance: {accounts[acc_no]['balance']}")
    else:
        print("Account not found")

import os


def customer_info():
    name = input("Enter name: ")
    address = input("Enter address: ")
    username = input("Enter username: ")
    userpassword = input("Enter user password: ")
    
    return name, address, username, userpassword  


def create_next_customer_id():
    if not os.path.exists("customers.txt"):  
        return "c001"
    else:
        with open("customers.txt", 'r') as file:
            lines = file.readlines() 
            if not lines:  
                return "c001"
            last_line = lines[-1].split("\t")[0] 
            last_id = int(last_line[1:])  
            return f'c{last_id + 1}' 


def create_customer():
    customer = customer_info() 
    customer_id = create_next_customer_id()  
    
    with open("customers.txt", 'a') as customers_file, open("users.txt", 'a') as users_file:
        customers_file.write(f'{customer_id}\t{customer[0]}\t{customer[1]}\n')  
        users_file.write(f'{customer[2]}\t{customer[3]}\n')  
        
    print(f"Customer {customer_id} added successfully!")



def save_transaction():
    acc_no=input("Enter account number:")
    
    with open("transactions.txt", "a") as file:  
        file.write(f"{acc_no}/t{save_transaction}\n")





while True:
    print("\n****** Banking System Menu ******")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transactions")
    print("5.check balance")
    print("6. User Login")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
        print("**********")
    elif choice == "2":
        deposit()
        print("**********")
    elif choice == "3":
        withdraw()
        print("**********")
    elif choice == "4":
        view_transactions()
        print("**********")
    elif choice == "5":
        check_balance()
        print("**********")
    elif choice == "6":
        user_login()
        print("**********")
        break
    elif choice == "7":
         print("Exiting system... Thank you!")
         print("**********")
    else:
        print("Invalid choice! Please try again.")
 

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







