Even = lambda a : a % 2 == 0
Square = lambda a : a ** 2
Sum = lambda a, b : a  + b
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
    result = 0
    for i in Values:
        result = (Task(result,i))
    return result

def main():
    Data = []
    size = int(input("Enter the how many elements to insert: "))
    
    print("Enter the Numeric Value only")
    
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    print(Data)
    
    FData = list(FilterX(Even , Data))
    print(FData)
    
    MData = list(MapX(Square , FData))
    print(MData)
    
    RData = ReduceX(Sum , MData)
    print(RData)
    
if __name__ == "__main__":
    main()