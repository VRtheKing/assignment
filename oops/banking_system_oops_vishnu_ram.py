class Account:
    def __init__(self, account_number, balance,account_name):
        self.account_name=account_name
        self.account_number=account_number
        self.balance=balance
        # self.age=age
        # self.gender=gender

    def view_acc_details(self):
        print("\nYour Account Details: ")
        print(f"Your Account Type: {type(self).__name__}")
        print(f"Account Holder: {self.account_name}")
        if isinstance(self,Savings):
            print(f"Your Account Balance {self.balance}")
        else:
            print(f"Your due bill is: {self.balance}")

class Savings(Account):
    def __init__(self, account_number, account_name, balance=0):
        Account.__init__(self, account_number, balance, account_name)

    def show_options(self):
        print("""\n1. View balance.
2. Deposit 
3. Withdraw
4. View Account Details
0. Main Menu""")

    def view_balance(self):
        print(f"\nYour Balance is Rs. {self.balance}")

    def deposit(self, amount):
        self.balance+=amount
        print(f"\nRs. {amount} deposited. Your balance is Rs. {self.balance}")

    def withdraw(self, amount):
        if self.balance-amount >= 0:
            self.balance-=amount
            print(f"\nRs. {amount} withdrawn. Your balance is Rs. {self.balance}")
        else:
            print(f"\nInsufficient Balance: Rs. {self.balance}")


class Credit(Account): 
    def __init__(self, account_number, account_name, limit, due, balance=0):
        Account.__init__(self, account_number, balance, account_name)
        self.limit=limit
        self.due=due

    def show_options(self):
        print("""\n1. View bill.
2. Deposit 
3. Withdraw
4. View Account Details
0. Main Menu""")
    
    def view_bill(self):
        print(f"\nYour bill is Rs. {self.due}. Your credit limit is Rs. {self.limit}")

    def deposit(self, amount):
        if self.due-amount<0:
            print(f"The amount is over the current bill amount: {self.due}")
        else:
            self.due-=amount
            print(f"\nRs. {amount} deposited. Your bill is now Rs. {self.due}")
        self.balance=self.due

    def withdraw(self, amount):
        if self.limit>=self.due+amount:
            self.due+=amount
            print(f"\nRs. {amount} withdrawn. Your bill is Rs. {self.due}. Available Limit is Rs. {self.limit-self.due}")
        else:
            print(f"\nInsufficient Credit: Rs. {self.limit-self.balance} (Limit: {self.limit})")
        self.balance=self.due


Accounts=[]

while True:
    print("Welcome to XYZ Bank.")
    acc_num=int(input("> Enter account number: "))
    curr_acc=None
    for i in Accounts:
        if i.account_number==acc_num:
            curr_acc=i
            break
    if curr_acc is None:
        print("New account creation:")
        prompt=input("Account type (S)avings / (C)redit: ").upper()
        if prompt =='S':
            name=input("> Enter Account Holders Name: ")
            savings_acc =Savings(acc_num, name)
            print("Savings account created.")
            Accounts.append(savings_acc)
            curr_acc=savings_acc 
        elif prompt=='C':
            name=input("> Enter Account Holders Name: ")
            limit=int(input("> Enter Credit Limit: "))
            credit_acc=Credit(acc_num,name,limit,0,0)
            print("Credit Account Created.")
            Accounts.append(credit_acc)
            curr_acc=credit_acc 
        else:
            print("Enter Valid Account Type. (C|S)")
            continue
    curr_acc.view_acc_details()
    while True:
        curr_acc.show_options()
        option=int(input("> Enter the option: "))
        
        if isinstance(curr_acc,Savings):
            if option==1:
                curr_acc.view_balance()
            elif option==2:
                dep=int(input("> Enter the amount to deposit: "))
                curr_acc.deposit(dep)
            elif option==3:
                wd=int(input("> Enter the amount to withdraw: "))
                curr_acc.withdraw(wd)
            elif option==4:
                curr_acc.view_acc_details()
            elif option==0:
                break 

        elif isinstance(curr_acc,Credit):
            if option==1:
                curr_acc.view_bill()
            elif option==2:
                dep=int(input("> Enter the amount to deposit: "))
                curr_acc.deposit(dep)
            elif option==3:
                wd=int(input("> Enter the amount to withdraw: "))
                curr_acc.withdraw(wd)
            elif option==4:
                curr_acc.view_acc_details()
            elif option==0:
                break