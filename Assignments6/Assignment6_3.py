def PrintTable(num):
    for i in range(1,11):
        print(num , "*" , i , "= ",num * i)
        
def main():
    no = int(input("Enter the number: "))
    PrintTable(no)

if __name__ == "__main__":
    main()