def Divisible(number):
    if(number % 5 == 0):
        return True
    else:
        return False
    
        
def main():
    print(Divisible(8))
    print(Divisible(25))
    
    
if __name__ == "__main__":
    main()