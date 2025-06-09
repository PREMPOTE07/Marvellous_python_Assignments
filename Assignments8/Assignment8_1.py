import threading

def even():
    print("Inside even")
    for i in range(2,12,2):
        print(i)

def odd():
    print("Inside odd")
    for i in range(1,10,2):
        print(i)

def main():
    print("Inside main")
    T1 = threading.Thread(target=even)
    T2 = threading.Thread(target=odd)
    
    T1.start()
    T2.start()
    
    T1.join  # waiting state
    T2.join  # waiting state

if __name__ == "__main__":
    main()