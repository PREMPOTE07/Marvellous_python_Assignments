def sum_n(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

def recSum_n(n):
    if n == 0:
        return 0
    return n + recSum_n(n-1)

def main():
    print(sum_n(5))
    print(recSum_n(5))

if __name__ == "__main__":
    main()