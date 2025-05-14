def CalSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num %  10
        num =  num // 10
        
    return sum
    
def main():
    no = int(input("Enter the number: "))
    print("Sum is: ",CalSumOfDigits(no))

if __name__ == "__main__":
    main()