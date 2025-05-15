def prime(n):
    if n <= 1 :
        return False
    
    for i in range(2,int(n ** 0.5) + 1 ):
        if n % i == 0:
            return False
    return True
def main():
     numbers = []
     size = int(input("Enter the size: "))
     for i in range(size):
         no = int(input())
         numbers.append(no)
         
     FData = list(filter(prime,numbers))
     print("Prime list : ",FData)
    
if __name__ == "__main__":
    main()