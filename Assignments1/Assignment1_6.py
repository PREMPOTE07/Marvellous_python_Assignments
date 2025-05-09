def check(number):
    if(number == 0):
        print("Zero")
    elif(number > 0):
        print("Positive")
    else:
        print("Negative")
        
def main():
    check(0)
    check(10)
    check(-10)
    
if __name__ == "__main__":
    main()