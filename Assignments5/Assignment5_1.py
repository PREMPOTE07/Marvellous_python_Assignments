sum = lambda a , b : a + b
diff = lambda a, b : a - b
prod = lambda a , b : a * b
div = lambda a , b : a / b

def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the seccond number: "))
    print("Sum: ",sum(no1,no2))
    print("Difference: ",diff(no1,no2))
    print("Product: ",prod(no1,no2))
    print("Division: ",div(no1,no2))

if __name__=="__main__":
    main()