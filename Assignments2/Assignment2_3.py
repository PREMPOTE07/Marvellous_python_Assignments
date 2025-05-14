def fact(num):
    temp = 1
    for i in range(num):
        temp+= temp * i
    print("Factorial is : ",temp)
def main():
    no = int(input("Enter the Number: "))
    fact(no)

if __name__ == "__main__":
    main()