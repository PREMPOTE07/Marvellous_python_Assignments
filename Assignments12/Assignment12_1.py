class Demo:
    Value = 0 # class variable
    
    def __init__(self):
        self.no1 = int(input("Enter first Number: "))      # instance variable
        self.no2 = int(input("ENter second Number: "))       # instance variable
        
    def Fun(self): # instance method    
         print("First Number: ",self.no1)
         print("Second Number: ",self.no2)
    
    def Gun(self): # instance method
        print("First Number: ",self.no1)
        print("Second Number: ",self.no2)
    
def main():
    obj1 = Demo()
    obj2 = Demo()
    
    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()