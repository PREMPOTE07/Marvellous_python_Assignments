# find largest among three numbers
def FindLargest(a,b,c):
    if a > b and c:
        print(a,"is The Largest")
    elif b > a and c:
        print(b,"is The Largest")
    else:
        print(c,"is The Largest")
        
def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))
    no3 = int(input("Enter the third number: "))
    FindLargest(no1,no2,no3)
    
if __name__ == "__main__":
    main()