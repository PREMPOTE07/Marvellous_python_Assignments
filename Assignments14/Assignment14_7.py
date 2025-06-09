class Person:
    def __init__(self,A,B):
        print("Inside person class")
        self.name = A
        self.age = B

class Teacher(Person):
    def __init__(self, A, B):
        print("Inside Teacher Class")    
        super().__init__(A, B)
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
            
def main():
   obj = Teacher("prem",21)
   obj.Display()

if __name__ == "__main__":
    main()