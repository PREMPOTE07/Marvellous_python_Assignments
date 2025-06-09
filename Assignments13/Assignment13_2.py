class BankAccount:
    ROI = 10.5   # rate of interset as a class variable
    def __init__(self):
        self.Name = input("Enter Name: ")
        self.Amount = int(input("Enter Amount: "))
    
    def Deposit(self):
        DepositAMt = int(input("Enter Amount to deposit: "))
        self.Amount = self.Amount + DepositAMt 
        
    def Withdraw(self):
        withDrawAmt = int(input("Enter amount to withdraw: "))
        if withDrawAmt > self.Amount:
            print("Insuffienct balance")
        else:
            self.Amount = self.Amount - withDrawAmt


    def CalculateInterest(self):
        Interest = (self.Amount  *  BankAccount.ROI ) / 100
        print("Interse on amount: ",Interest)
        self.Amount = self.Amount - Interest
    
    def Display(self):
        print("Name: ",self.Name)
        print("Amount: ",self.Amount) 
    
def main():
    obj1 = BankAccount()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()
    
    obj2 = BankAccount()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()

if __name__ == "__main__":
    main()