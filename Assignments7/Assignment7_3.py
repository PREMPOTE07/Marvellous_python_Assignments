
def main():
     numbers = []
     size = int(input("Enter the size: "))
     for i in range(size):
         no = int(input())
         numbers.append(no)
         
     FData = list(filter(lambda a : a % 2 == 0 ,numbers))
     print("Even List: ",FData)
    
if __name__ == "__main__":
    main()