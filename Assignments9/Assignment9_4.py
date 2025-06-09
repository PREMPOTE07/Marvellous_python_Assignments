import multiprocessing.process
import threading
import multiprocessing
import time


def sumNum():
    print("Inside sum function")
    sum = 0
    for i in range(1,1000001):
        sum = sum + i
    print("Sum is : ",sum)
    
def main():
    print("Inside main function")
    
    #print using normal function
    start_time = time.time()
    sumNum()
    end_time = time.time()
    print("Time required for normal fun: ",end_time - start_time)
    
    #print using threading
    start_time = time.time()
    T = threading.Thread(target=sumNum)
    T.start()
    T.join()
    end_time = time.time()
    print("Time required for threadign: ",end_time - start_time)
    
    #print using multiprocessigng
    start_time = time.time()
    P = multiprocessing.Process(target=sumNum)
    P.start()
    P.join()
    end_time = time.time()
    print("Time reaquired for multiprocessing: ",end_time - start_time)
    
    
if __name__ == "__main__":
    main()