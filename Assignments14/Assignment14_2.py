class Rectangle:
    def __init__(self,A,B):
        self.length = A
        self.width = B
    
    def CalArea(self):
        return self.length * self.width
    
    def CalPerimeter(self):
        return 2 * (self.length + self.width)
    
        
    
def main():
    rect1 = Rectangle(10,5)
    print("Area: ",rect1.CalArea())
    print("Perimeter: ",rect1.CalPerimeter())

if __name__ == "__main__":
    main()