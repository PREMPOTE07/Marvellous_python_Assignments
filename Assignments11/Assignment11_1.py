i = 1
   
def PrintNum(n):
    for i in range(1,n+1):
        print(i,end=" ")
     
def recPritnNum(n):
    global i
    if  i <= n:
        print(i,end=" ")
        i = i + 1
        recPritnNum(n)   
         
def main():
    PrintNum(5)
    recPritnNum(5)

if __name__ == "__main__":
    main()