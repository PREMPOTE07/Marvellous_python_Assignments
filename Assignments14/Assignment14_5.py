class BankAccount:
    def __init__(self,A,B,C):
        self.Account_number = A
        self.name = B
        self.balance = C
        
    def deposit(self,A):
        self.balance = self.balance + A
        
    def withdraw(self,A):
        self.balance = self.balance - A
        
    def display(self):
        print("Balance: ",self.balance)
    
def main():
    cust1 = BankAccount("12345678910111","Prem",43250)
    cust1.deposit(500)
    cust1.withdraw(250)
    cust1.display()

if __name__ == "__main__":
    main()