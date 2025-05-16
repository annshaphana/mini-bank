account_number={}
transactions={}
def count_transaction():
    
    total=len((transactions.get(account_number, [])))
    print(f"Total transaction for account(account_number): (total) ")

count_transaction(account_number,transactions)    