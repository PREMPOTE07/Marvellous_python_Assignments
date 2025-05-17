def CheckPrime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def main():
    no = int(input("Enter the Number: "))
    if no > 1:
        result = ChkPrime(no)
        if result:
           print("Given Number is Prime")
        else:
           print("Given Number is Not Prime")
    else:
        print("Please Enter Number > 1")

if __name__ == "__main__":
    main()
