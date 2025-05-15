from functools import reduce
def main():
     numbers = []
     size = int(input("Enter the size: "))
     for i in range(size):
         no = int(input())
         numbers.append(no)
         
     RData = reduce(lambda a , b: a * b ,numbers)
     print("Product is: ",RData)
    
if __name__ == "__main__":
    main()