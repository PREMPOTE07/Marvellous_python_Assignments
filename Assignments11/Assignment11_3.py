def SOD(num):
    sum = 0
    while(num > 0 ):
        sum  = sum + num % 10
        num = num // 10
    return sum

def recSOO(num):
    if num == 0:
        return 0
    return num % 10 + recSOO(num // 10)
    
def main():
    print(SOD(1234))
    print(recSOO(1234))

if __name__ == "__main__":
    main()