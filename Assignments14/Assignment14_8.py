class Vehicle:
    def Start(self,A):
        print(A+2)
        print("Vehicle start")
        
        
class Car(Vehicle):
    def Start(self,A):
        print(A+1)
        print("Car Start")
        
def main():
    vobj = Vehicle()
    cobj  = Car()
    
    vobj.Start(2)
    cobj.Start(2)

if __name__ == "__main__":
    main()