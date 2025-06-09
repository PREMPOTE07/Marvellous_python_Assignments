class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
    def Accept(self):
        self.Value1 = int(input("Enter the first number: "))
        self.Value2 = int(input("Enter the second number: "))
    
    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 *  self.Value2
    
    def Division(self):
        try:   
            return self.Value1 /  self.Value2
            
        except ZeroDivisionError:
            return "Cant divisible by zero"
    

def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()
    
    obj1.Accept()
    print(obj1.Addition())
    print(obj1.Substraction())
    print(obj1.Multiplication())
    print(obj1.Division())
    
    obj2.Accept()
    print(obj2.Addition())
    print(obj2.Substraction())
    print(obj2.Multiplication())
    print(obj2.Division())
    
    

if __name__ == "__main__":
    main()