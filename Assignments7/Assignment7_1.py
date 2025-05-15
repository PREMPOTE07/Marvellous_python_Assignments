Square = lambda a : a ** 2
Cube = lambda a : a ** 3

def main():
    no = int(input("Enter the number: "))
    print("Square: ",Square(no))
    print("Cube: ",Cube(no))
    
if __name__ == "__main__":
    main()