import multiprocessing
import os

def calSquare(list):
    print("PID of Process: ",os.getpid())
    print("PPID of Process: ",os.getppid())
    empty = []
    for i in list:
        empty.append(i**2)
    
    print("List is : ",empty)
        
    
def main():
    print("Inside Main")
    print("PID of main process : ",os.getpid())
    
    Nums = [2,4,6,9]
    
    P1 = multiprocessing.Process(target=calSquare,args=(Nums,))
    P2 = multiprocessing.Process(target=calSquare,args=(Nums,))
    
    P1.start()
    P1.join()
    
    P2.start()
    P2.join()
    

if __name__ == "__main__":
    main()