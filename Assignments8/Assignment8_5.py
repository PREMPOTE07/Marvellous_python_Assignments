import threading

def DisplayOTF():
    print("1 TO 50")
    for i in range(1,51,1):
        print(i)
        

def DisplayFTO():
    print("50 TO 1")
    for i in range(50,0,-1):
        print(i)
        

def main():
    print("Inside main")
    
    Thread1 = threading.Thread(target=DisplayOTF)
    Thread2 = threading.Thread(target=DisplayFTO)
    
    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()
    
    print("End of main")

if __name__ == "__main__":
    main()