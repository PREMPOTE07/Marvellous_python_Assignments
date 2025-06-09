import multiprocessing

def Fact(no):
    print("Inside Fact function")
    sum = 1
    for i in range(1,no+1):
        sum = sum * i
    print("Fact is: ",sum)
        
def main():
    print("Inside Main")
    
    p = multiprocessing.Pool(Fact(5))
    
    p.close()
    p.join()
    


if __name__ == "__main__":
    main()