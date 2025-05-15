def EvenOdd(num):
    if num % 2 ==  0:
        print(num, "is a Even")
    else:
        print(num,"is a Odd")

def main():
    no = int(input("Enter the number: "))
    EvenOdd(no)
    
if __name__ == "__main__":
    main()