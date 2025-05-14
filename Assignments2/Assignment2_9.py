def CountLen(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
    
def main():
    no = int(input("Enter the number: "))
    print(CountLen(no))

if __name__ == "__main__":
    main()