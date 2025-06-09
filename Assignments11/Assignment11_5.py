count = 0
def countZeros(num):
    count = 0
    while num > 0:
        rem = num % 10 
        if rem == 0:
            count = count + 1
        num = num // 10
    return count

def recCountZeros(num):
    if num == 0:
        return 0
    if num % 10 == 0:
        return 1 + recCountZeros(num // 10)
    else:
        return recCountZeros(num // 10)
    
def main():
    print(countZeros(1020300))
    print(recCountZeros(1020300))

if __name__ == "__main__":
    main()