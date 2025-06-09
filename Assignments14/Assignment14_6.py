class Calculator:
    def __init__(self):
        self.val1 = float(input("Enter first number: "))
        self.val2 = float(input("Enter second number: "))
        
    def Add(self):
        return self.val1 + self.val2
    
    def Sub(self):
        return self.val1 - self.val2
    
    def Mult(self):
        return self.val1 * self.val2
    try:
        def Div(self):
           return self.val1 / self.val2    
    except ZeroDivisionError:
        print("Cant divisible by zero")
    
def main():
   cal1 = Calculator()
   print("Addition: ",cal1.Add())
   print("Multiplication: ",cal1.Mult())
   print("Subtraction: ",cal1.Sub())
   print("Division: ",cal1.Div())

if __name__ == "__main__":
    main()