import threading

def evenfactor(num):
    print("Inside evenfactor")
    sum = 0
    for i in range(2,num,2):
        sum = sum + i
    print("EvenFactor sum is: ",sum)

def oddfactor(num):
    print("Inside Oddgactor")
    sum = 0
    for i in range(1,num,2):
        sum = sum + i
    print("OddFactor sum is: ",sum)
        

def main():
    print("Inside main")
    val = int(input("Enter the number for evenfactor and oddfactor addition: "))
    
    T1 = threading.Thread(target=evenfactor , args=(val,))
    T2 = threading.Thread(target=oddfactor , args=(val,))
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
    print("exit form main")

if __name__ == "__main__":
    main()