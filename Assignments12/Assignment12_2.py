class Circle:
    PI = 3.14 # class variable
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumerence = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter Radius of circle: "))
    
    def CalArea(self):
        self.Area = Circle.PI * ( self.Radius * self.Radius )
    
    def CalCircumference(self):
        self.Circumerence = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius is: ",self.Radius)
        print("Area is: ",self.Area)
        print("Circumferce is: ",self.Circumerence)
        
def main():
    obj = Circle()
    obj2 = Circle()
    
    print("first circle")
    obj.Accept()
    obj.CalArea()
    obj.CalCircumference()
    obj.Display()
    
    print("second circle")
    obj2.Accept()
    obj2.CalArea()
    obj2.CalCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()