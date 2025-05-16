import datetime



def show_current_date():
    currentdate=datetime.now().strtime("%Y-%m-%d")
    
    print("date")
    print("2.time")
    print("3.exit")

    choice=input("Enter choice:")

    if choice=="1":
        withdraw()
    elif choice=="2":
        deposit()
    else:
        print("exit")
show_current_date()