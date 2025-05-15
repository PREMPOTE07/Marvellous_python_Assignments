def PrintPattern(num):
    for i in range(num+1):
        for j in range(i):
            print("* " , end="")
        print()
def main():
    n = int(input("Enter the number: "))
    PrintPattern(5)
    
if __name__ == "__main__":
    main()
        
        