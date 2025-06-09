import threading
import time

def printNum():
    for i in range(1,6):
        print(i)
    time.sleep(1)
    
def main():
    print("Inside Main")
    
    T1 = threading.Thread(target=printNum)
    T2 = threading.Thread(target=printNum)
    T3 = threading.Thread(target=printNum)
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()
    
    T3.start()
    T3.join()
    
    print("End of main")

if __name__ == "__main__":
    main()