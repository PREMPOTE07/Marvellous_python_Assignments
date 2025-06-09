class Product:
    def __init__(self,A,B):
        self.name = A
        self.price = B
    
    def __eq__(self,other):
        return (self.name,self.price) == (other.name,other.price)    

def main():
    prod1= Product("Pen",10)
    prod2 = Product("Pen",10)
    prod3 = Product("Notebook",10)
    
    print(prod1.__eq__(prod2)) # True
    print(prod1.__eq__(prod3)) # False
    

if __name__ == "__main__":
    main()