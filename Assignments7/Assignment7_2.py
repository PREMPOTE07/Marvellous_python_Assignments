
def main():
     numbers = []
     size = int(input("Enter the size: "))
     for i in range(size):
         no = int(input())
         numbers.append(no)
         
     MData = list(map(lambda a : a * 2 ,numbers))
     print("Doubled List: ",MData)
    
if __name__ == "__main__":
    main()