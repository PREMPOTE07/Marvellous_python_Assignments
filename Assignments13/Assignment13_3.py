class Numbers:
    def __init__(self):
        self.value = int(input("Enter the number: "))
        
    def ChkPrime(self):
        for i in range(2,self.value):
            if self.value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum = sum + i
        
                
        if sum == self.value:
            return True
        
        return False
    
    def Factors(self):
        print("Factors: ",end=" ")
        for i in range(1,self.value):
            if self.value % i == 0:
                print(i,end=" ")
        print()
    
    def SumFactors(self):
        sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum = sum + i
        return sum
        
        
            

def main():
    obj1 = Numbers()
    
    if obj1.ChkPrime() == True:
        print("Number is prime")
    else:
        print("Number is not prime")
        
        
    if obj1.ChkPerfect() == True:
        print("Number is perfect")
    else:
        print("Number is not perfect")
    
    obj1.Factors()
    
    print("Sum of factors: ",obj1.SumFactors())

if __name__ == "__main__":
    main()