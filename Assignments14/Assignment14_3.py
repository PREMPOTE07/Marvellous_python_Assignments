class Book:
    def __init__(self,A):
        self.__price = A
       
    def setPrice(self,A):
        self.__price = A
        
    def getPrice(self):
        return self.__price
         
    
    
def main():
    B1 = Book(549)
    
    print("Price before Set: ",B1.getPrice())
    
    B1.setPrice(499)
    
    print("Price after set: ",B1.getPrice())

if __name__ == "__main__":
    main()