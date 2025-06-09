def power(x,n):
    result = 1
    for i in range(n):
        result = result * x
    return result

def recPower(x,n):
    if n == 0:
        return 1
    return x * recPower(x,n-1)

def main():
    print(power(2,3))
    print(recPower(2,3))

if __name__ =="__main__":
    main()