GreaterTS = lambda a : a >= 70 and a <= 90
SmallerTN = lambda a : a + 10
Product = lambda a, b : a * b
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
    result = 1
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
    
    FData = list(FilterX(GreaterTS , Data))
    print(FData)
    
    MData = list(MapX(SmallerTN , FData))
    print(MData)
    
    RData = ReduceX(Product , MData)
    print(RData)
    
if __name__ == "__main__":
    main()