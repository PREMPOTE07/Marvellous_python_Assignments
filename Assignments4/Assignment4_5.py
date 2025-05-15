def CheckPrime(num):
    if num > 1:
     for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return False
    return True

MultiplyBT = lambda a : a  * 2
MaxNum = lambda a, b : b >= a
def FilterX(Task , Values):
    result = []
    
    for i in Values:
        if Task(i) == True:
            result.append(i)
    
    return result

def MapX(Task , Values):
    result = []
    
    for i in Values:
        result.append(Task(i))
    
    return result
    
    
def ReduceX(Task , Values):
    for i in Values:
        result = 0
        if Task(result , i) == True:
            result = i
    return result
    

def main():
    Data = []
    size = int(input("Enter the how many elements to insert: "))
    
    print("Enter the Numeric Value only")
    
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    print(Data)
    
    FData = list(FilterX(CheckPrime , Data))
    print(FData)
    
    MData = list(MapX(MultiplyBT , FData))
    print(MData)
    
    RData = ReduceX(MaxNum , MData)
    print(RData)
    
if __name__ == "__main__":
    main()