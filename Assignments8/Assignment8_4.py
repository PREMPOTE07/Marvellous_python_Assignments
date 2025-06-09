import threading
def smallChar(string):
    print("Inside small Characters function")
    print("small Thread id: ",threading.get_ident())
    for i in string:
        if i.islower():
            print(i)
            
def capitalChar(string):
    print("Inside capital Characters function")
    print("capital Thread id: ",threading.get_ident())
    for i in string:
        if i.isupper():
            print(i)
            
def digitChar(string):
    print("Inside digit Characters function")
    print("digit Thread id: ",threading.get_ident())
    for i in string:
        if i.isdigit():
            print(i)
def main():
    print("Inside Main")
    
    str = input("Enter the string: ")
    
    small = threading.Thread(target=smallChar,args=(str,))
    capital = threading.Thread(target=capitalChar,args=(str,))
    digit = threading.Thread(target=digitChar,args=(str,))
    
    small.start()
    small.join()
    
    capital.start()
    capital.join()
    
    digit.start()
    digit.join()    
    
    print("End of main")

if __name__ == "__main__":
    main()