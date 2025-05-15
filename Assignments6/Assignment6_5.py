def CheckPrime(num):
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    n = int(input("Enter the number: "))
    if CheckPrime(n) == True:
        print(n , "is a Prime Number")
    else:
        print(n,"is Not a Prime Number")
    
if __name__ == "__main__":
    main()
        
        