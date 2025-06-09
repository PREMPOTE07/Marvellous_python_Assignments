def Fact(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum
    
     
def recFact(n):
    if n <= 1:
        return 1
    return n * recFact(n-1)
           
              
def main():
    print(Fact(5))
    print(recFact(5))
   

if __name__ == "__main__":
    main()