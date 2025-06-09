def printStar(num):
    for i in range(num+1):
        for j in range(i):
            print("*",end=" ")
        print()
        
def recPrintStar(num,i,j): # i for rows and j for columns
    if j > i:
        return
    print("* " * j)
    recPrintStar(num , i , j + 1)
        
def main():
    printStar(4)
    recPrintStar(4,4,0)

if __name__ == "__main__":
    main()