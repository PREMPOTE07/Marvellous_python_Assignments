def Fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
def main():
    n = int(input("Enter the number: "))
    print("Factorial of ",n,"is: ",Fact(n))
    
if __name__ == "__main__":
    main()
        
        