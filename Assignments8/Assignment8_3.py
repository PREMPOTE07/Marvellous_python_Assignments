import threading

def addEvenList(list):
    print("Inside addEvenList")
    sum = 0
    for i in list:
        sum = sum + i
    
    print("Addition of evenlist is : ",sum)
    
def addOddList(list):
    print("Inside addOddList")
    sum = 0
    for i in list:
        sum = sum + i
    
    print("Addition of oddlist is : ",sum)    
        
def main():
    print("Inside Main")
    
    EvenList = [4,12,14,72,48]
    OddList =  [5,11,13,17,71]
    
    T1 = threading.Thread(target=addEvenList , args=(EvenList,))
    T2 = threading.Thread(target=addOddList , args=(OddList,))
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
    print("End of Main")
    
    

if __name__ == "__main__":
    main()