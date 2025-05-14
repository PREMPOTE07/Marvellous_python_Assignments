def Addfact(num):
    temp = 0
    for i in range(1,num-1):
        if(num % i == 0):
            temp += i
    print("Addition of Factors is : ",temp)
def main():
    no = int(input("Enter the Number: "))
    Addfact(no)

if __name__ == "__main__":
    main()