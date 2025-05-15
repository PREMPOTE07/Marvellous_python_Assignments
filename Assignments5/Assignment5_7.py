Area = lambda a , b : a * b
Perimeter = lambda a , b : 2 * (a+b)

def main():
    len = int(input("Enter the Length of a Rectangle : "))
    width = int(input("Enter the Width of a Rectangle : "))
    
    print("Area is : ",Area(len,width))
    print("Perimeter is : ",Perimeter(len,width))
    
if __name__ == "__main__":
    main()
    